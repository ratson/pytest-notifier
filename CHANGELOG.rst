==========
Change Log
==========

1.0.3 (2019-9-23)
==================

- Compatibility with pytest 5


1.0.2 (2017-12-24)
==================

- Fix failed message typo (`#8 <https://github.com/ratson/pytest-notifier/pull/8>`_)


1.0.1 (2017-07-01)
==================

- Fix ``terminal-notifier`` crash (`#6 <https://github.com/ratson/pytest-notifier/pull/6>`_)


1.0.0 (2017-03-31)
==================

**New Features**

- Add ``--notifier-off`` option

**Behavioural Changes**

- Remove all old options
- Count setup errors as failed
- Update notificaiton message with emoji and pytest icon


0.3.1 (2017-01-21)
==================

- Avoid subprocess.CalledProcessError when interrupted


0.3 (2016-06-15)
================

**New Features**

- Allow override notifier titles based on zero/pass/fail (`#1 <https://github.com/ratson/pytest-notifier/pull/1>`_)

**Behavioural Changes**

- Exclude setup/teardown from test counts (`#2 <https://github.com/ratson/pytest-notifier/pull/2>`_)


0.2 (2016-01-09)
================

- Add libnotify support


0.1 (2016-01-07)
================

- Initial public release
