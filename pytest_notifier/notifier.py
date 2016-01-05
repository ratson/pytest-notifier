import subprocess


def notify_via_terminal_notifier(title, body):
    subprocess.check_call([
        'terminal-notifier', '-title', title, '-subtitle', body,
    ])


def notify_via_apple_script(title, body):
    command = [
        'osascript', '-e',
        'display notification "{body}" with title "{title}"'
        ''.format(title=title, body=body),
    ]
    p = subprocess.Popen(command)
    p.wait()


def notify(title, body):
    for f in (
        notify_via_terminal_notifier,
        notify_via_apple_script,
    ):
        try:
            f(title, body)
        except OSError:
            pass
        else:
            break
