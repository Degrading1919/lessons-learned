"""Sanitize/reconcile local Caelmor development counters; never publish raw logs.

Usage: py -3 scripts/extract_caelmor_session_metrics.py --root-log <rollout.jsonl>
Child IDs are read from the existing case measurement, not discovered by scanning
unrelated chats. No prompts, tool outputs, reasoning text or account IDs are emitted.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'evidence/measurements/2026-11-02-caelmor-session-metrics.json'
CUTOFF = '2026-11-03T04:09:25.235Z'
FIELDS = ('input_tokens', 'cached_input_tokens', 'output_tokens',
          'reasoning_output_tokens', 'total_tokens')


def source_records(path):
    with path.open('rb') as stream:
        for number, raw in enumerate(stream, 1):
            record = json.loads(raw)
            if record['timestamp'] >= CUTOFF:
                return
            yield number, raw, record


def extract(path, task, global_ids):
    totals = Counter()
    ids = set()
    duplicates = 0
    digest = hashlib.sha256()
    contexts = set()
    rates = {}
    last_snapshot = None
    record_count = 0
    last_line = 0
    completed_turns = []
    for number, raw, record in source_records(path):
        digest.update(raw)
        record_count += 1
        last_line = number
        payload = record.get('payload', {})
        if record['type'] == 'event_msg' and payload.get('type') == 'task_complete':
            error = payload.get('error') or {}
            completed_turns.append({'source_line': number, 'timestamp': record['timestamp'],
                                    'duration_ms': payload.get('duration_ms'),
                                    'error_code': error.get('codex_error_info'),
                                    'has_error': bool(error)})
        if record['type'] == 'turn_context':
            contexts.add((payload.get('model'), payload.get('effort')))
        if record['type'] == 'token_usage_record':
            response = payload['response_id']
            if response in global_ids:
                duplicates += 1
                continue
            global_ids.add(response)
            ids.add(response)
            for field in FIELDS:
                totals[field] += payload['usage'].get(field, 0)
            last_snapshot = {field: payload['thread_token_usage'].get(field, 0)
                             for field in FIELDS}
        if record['type'] == 'event_msg' and payload.get('type') == 'token_count':
            for kind in ('primary', 'secondary'):
                rate = (payload.get('rate_limits') or {}).get(kind)
                if not rate:
                    continue
                key = (kind, rate['window_minutes'], rate['resets_at'])
                sample = {'timestamp': record['timestamp'], 'source_line': number,
                          'used_percent': rate['used_percent']}
                bucket = rates.setdefault(key, {'first': sample, 'last': sample})
                bucket['last'] = sample
    return {
        'task': task, 'source_file': path.name,
        'source_prefix_sha256': digest.hexdigest(), 'records_before_cutoff': record_count,
        'last_included_line': last_line,
        'observed_model_effort': [dict(model=m, effort=e) for m, e in sorted(contexts)],
        'unique_responses': len(ids), 'duplicate_response_ids_skipped': duplicates,
        'usage_sum': dict(totals), 'last_thread_snapshot': last_snapshot,
        'usage_sum_matches_snapshot': dict(totals) == last_snapshot,
        'completed_turns': completed_turns,
        'rate_windows': [dict(kind=k, window_minutes=w, resets_at=r, **v)
                         for (k, w, r), v in rates.items()],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root-log', type=Path, required=True)
    args = parser.parse_args()
    prior = json.loads(TARGET.read_text(encoding='utf-8'))
    global_ids = set()
    records = [extract(args.root_log, 'orchestrator', global_ids)]
    for child in prior['child_attribution']:
        matches = list(args.root_log.parent.glob('*' + child['session_id'] + '.jsonl'))
        if len(matches) != 1:
            raise SystemExit(f"Expected one log for task {child['task']}, got {len(matches)}")
        records.append(extract(matches[0], child['task'], global_ids))
    combined = Counter()
    for item in records:
        combined.update(item['usage_sum'])
    prior['extraction'] = {
        'method': 'Unique response_id usage records before cutoff; cumulative snapshots not summed.',
        'cutoff_exclusive': CUTOFF,
        'global_unique_responses': len(global_ids),
        'duplicates_skipped': sum(r['duplicate_response_ids_skipped'] for r in records),
        'combined_logged_processing': dict(combined),
        'sessions': records,
    }
    prior['not_measured'] = {
        'api_dollars': None, 'task_attributable_subscription_percent': None,
        'human_attention_minutes': None, 'active_model_compute_wall_seconds': None,
        'controlled_model_comparison': None,
    }
    TARGET.write_text(json.dumps(prior, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'sessions': len(records), 'responses': len(global_ids),
                      'duplicates': prior['extraction']['duplicates_skipped'],
                      'logged_processing': dict(combined)}, indent=2))


if __name__ == '__main__':
    main()
