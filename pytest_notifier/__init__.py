"""pytest-notifier - A pytest plugin to notify test result"""
from time import time

from .notifier import notify


def pytest_addoption(parser):
    """
    Adds options to control notifications.
    """
    group = parser.getgroup('terminal reporting')
    group.addoption(
        '--notifier',
        dest='notifier',
        default=True,
        help='Enable test result notifications.',
    )


def get_msg_part(count, group):
    if not count:
        return None
    if group in ('passed', 'failed'):
        suffix = group.title()
    elif group == 'deselected':
        suffix = 'Skipped'
    elif group == 'error':
        suffix = 'Error(s)'
    return '{} {}'.format(count, suffix)


def pytest_terminal_summary(terminalreporter):
    if not terminalreporter.config.option.notifier:
        return

    tr = terminalreporter
    duration = time() - tr._sessionstarttime
    keys = ('passed', 'failed', 'error', 'deselected')
    counts = {k: len(tr.stats.get(k, [])) for k in keys}
    if sum(counts.values()) == 0:
        msg = 'No tests ran'
    elif counts['passed'] and not (counts['failed'] or counts['error']):
        msg = 'Success - {passed} Passed'.format(**counts)
    else:
        msg = ' '.join(filter(None, (
            get_msg_part(count=counts[k], group=k) for k in keys)))

    msg += ' in {:.2f}s'.format(duration)
    notify('py.test', msg)
