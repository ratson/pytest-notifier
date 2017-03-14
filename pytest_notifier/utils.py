import time
from collections import namedtuple


Info = namedtuple('Info', ['duration', 'total', 'passed', 'failed'])


def terminal_reporter_info(tr):
    duration = time.time() - tr._sessionstarttime
    passed = len(tr.stats.get('passed', []))
    failed = sum([len(tr.stats.get('failed', [])),
                  len(tr.stats.get('error', []))])
    return Info(
        duration=duration,
        total=passed + failed,
        passed=passed,
        failed=failed,
    )
