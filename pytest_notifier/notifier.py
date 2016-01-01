import subprocess


def notify(title, body):
    command = [
        'osascript', '-e',
        'display notification "{body}" with title "{title}"'
        ''.format(title=title, body=body),
    ]
    p = subprocess.Popen(command)
    p.wait()
