import time
from datetime import datetime

import pytest

from .utils import Info, terminal_reporter_info


@pytest.fixture(name='mock_time')
def mock_time_fixture(mocker):
    mock_time = mocker.Mock()
    mock_time.return_value = time.mktime(datetime(2047, 4, 1).timetuple())
    mocker.patch('time.time', mock_time)
    return mock_time


def test_terminal_reporter_info_duration(mocker, mock_time):
    m = mocker.MagicMock(
        _sessionstarttime=mock_time.return_value,
    )
    assert terminal_reporter_info(m) == Info(
        duration=0,
        total=0,
        passed=0,
        failed=0,
    )


def test_terminal_reporter_info_test_counts(mocker, mock_time):
    m = mocker.MagicMock(
        _sessionstarttime=mock_time.return_value,
        stats={
            'passed': [
                mocker.MagicMock(when='call'),
                mocker.MagicMock(when='call'),
            ],
            'failed': [
                mocker.MagicMock(when='call'),
            ],
        },
    )
    assert terminal_reporter_info(m) == Info(
        duration=0,
        total=3,
        passed=2,
        failed=1,
    )
