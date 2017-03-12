import sys
import subprocess


def notify_via_libnotify(title, body, icon=None):
    args = ['notify-send', title, body]
    subprocess.check_call(args)


def notify_via_terminal_notifier(title, body, icon=None):
    args = ['terminal-notifier', '-title', title, '-subtitle', body]
    if icon:
        args.extend(['-appIcon', icon])
    subprocess.check_call(args)


def notify_via_apple_script(title, body, **kwargs):
    command = [
        'osascript', '-e',
        'display notification "{body}" with title "{title}"'
        ''.format(title=title, body=body),
    ]
    p = subprocess.Popen(command)
    p.wait()


def notify(**kwargs):
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
            f(**kwargs)
        except OSError:
            pass
        else:
            break
