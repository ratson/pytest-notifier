"""pytest-notifier - A pytest plugin to notify test result"""
from time import time

from _pytest.main import EXIT_INTERRUPTED

from .notifier import notify
from .utils import terminal_reporter_info


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


def pytest_terminal_summary(terminalreporter, exitstatus):
    if not terminalreporter.config.option.notifier:
        return

    if exitstatus == EXIT_INTERRUPTED:
        return

    info = terminal_reporter_info(terminalreporter)

    if info.total == 0:
        return
    elif info.passed == info.total:
        title = '100% Passed'
        msg = '{} Passed'.format(info.passed)
    elif info.failed > 0:
        title = '{}% Faild'.format(int(info.failed * 100 / info.total))
        msg = '{0.failed} of {0.total} tests failed'.format(info)
    else:
        title = 'Unexpected Result'
        msg = 'Please report an issue how to trigger this'

    msg += ' in {:.2f}s'.format(info.duration)
    notify(title, msg)
