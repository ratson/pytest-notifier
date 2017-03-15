import time
from collections import namedtuple


Info = namedtuple('Info', ['total', 'passed', 'failed'])


def terminal_reporter_info(tr):
    passed = len(tr.stats.get('passed', []))
    failed = sum([len(tr.stats.get('failed', [])),
                  len(tr.stats.get('error', []))])
    return Info(
        total=passed + failed,
        passed=passed,
        failed=failed,
    )
