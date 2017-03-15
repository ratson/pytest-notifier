from .utils import Info, terminal_reporter_info


def test_terminal_reporter_info_test_counts(mocker):
    m = mocker.MagicMock(
        stats={
            'passed': [
                mocker.MagicMock(when='call'),
                mocker.MagicMock(when='call'),
            ],
            'failed': [
                mocker.MagicMock(when='call'),
            ],
            'error': [
                mocker.MagicMock(when='setup', outcome='failed'),
            ],
        },
    )
    info = terminal_reporter_info(m)
    assert info.total == 4
    assert info.passed == 2
    assert info.failed == 2
