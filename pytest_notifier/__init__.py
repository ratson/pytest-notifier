"""pytest-notifier - A pytest plugin to notify test result"""
from __future__ import unicode_literals
import os

try:
    # pytest < 5
    from _pytest.main import EXIT_INTERRUPTED
except ImportError:
    # pytest >= 5
    from _pytest.main import ExitCode
    EXIT_INTERRUPTED = ExitCode.INTERRUPTED

from .notifier import notify
from .utils import terminal_reporter_info


def pytest_addoption(parser):
    """
    Adds options to control notifications.
    """
    group = parser.getgroup('terminal reporting')
    group.addoption(
        '--notifier-off',
        action='store_true',
        dest='notifier_off',
        help='Turn off test result notifications.',
    )


def pytest_terminal_summary(terminalreporter, exitstatus):

    # If run together with pytest-xdist
    # We don't want to send notifications from workers
    if os.getenv('PYTEST_XDIST_WORKER'):
        return

    if terminalreporter.config.option.notifier_off:
        return

    if exitstatus == EXIT_INTERRUPTED:
        return

    info = terminal_reporter_info(terminalreporter)

    if info.total == 0:
        return
    elif info.passed == info.total:
        title = '100% Passed'
        msg = '\u2705 {} tests passed'.format(info.passed)
    elif info.failed > 0:
        title = '{}% Failed'.format(int(info.failed * 100 / info.total))
        msg = '\u26D4\uFE0F {0.failed} of {0.total} tests failed'.format(info)
    else:
        title = 'Unexpected Result'
        msg = 'Please report an issue how to trigger this'

    icon = os.path.join(os.path.dirname(__file__), 'pytest_logo.png')
    notify(title=title, body=msg, icon=icon)
