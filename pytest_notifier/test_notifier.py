import subprocess

from .notifier import notify_via_terminal_notifier


def test_notify_via_terminal_notifier(mocker):
    mocker.patch('subprocess.check_call')
    notify_via_terminal_notifier('title', 'body')
    subprocess.check_call.assert_called_once()
