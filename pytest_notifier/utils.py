import time
from collections import namedtuple


Info = namedtuple('Info', ['duration', 'total', 'passed', 'failed'])


def terminal_reporter_info(tr):
    duration = time.time() - tr._sessionstarttime
    keys = ('passed', 'failed', 'error', 'deselected')
    counts = {
        k: len(list(filter(lambda r: getattr(r, 'when', '') == 'call',
                           tr.stats.get(k, []))))
        for k in keys
    }
    return Info(
        duration=duration,
        total=sum(counts.values()),
        passed=counts.get('passed', 0),
        failed=counts.get('failed', 0),
    )
