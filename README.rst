pytest-notifier
===============

.. image:: https://img.shields.io/pypi/v/pytest-notifier.svg
    :target: https://pypi.python.org/pypi/pytest-notifier
    :alt: Latest PyPI version

A `pytest`_ plugin to notify test result on Linux and OS X.


Requirements
------------

Linux
^^^^^

Make sure ``notify-send`` is exists in ``$PATH``,
which comes from ``libnotify``.

OS X
^^^^

OS X 10.8 and higher is required.

Optionally, you could install `terminal-notifier`_
to avoid Script Editor being opened when notification icon is clicked.


Installation
------------

You can install "pytest-notifier" via `pip`_ from `PyPI`_::

    $ pip install pytest-notifier


Licence
-------

Distributed under the terms of the `MIT`_ license, "pytest-notifier" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`file an issue`: https://github.com/ratson/pytest-notifier/issues
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`terminal-notifier`: https://github.com/julienXX/terminal-notifier
