import sys
import subprocess


def notify_via_libnotify(title, body):
    subprocess.check_call([
        'notify-send', title, body,
    ])


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
    notify_functions = {
        'darwin': (notify_via_terminal_notifier,
                   notify_via_apple_script,
                   notify_via_libnotify),
        'linux': (notify_via_libnotify,),
    }.get(sys.platform, (notify_via_libnotify,
                         notify_via_terminal_notifier,
                         notify_via_apple_script,))
    for f in notify_functions:
        try:
            f(title, body)
        except OSError:
            pass
        else:
            break
