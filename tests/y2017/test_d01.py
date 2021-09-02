""" Day 01: Inverse Captcha """

import pytest
from advent_of_code.y2017.d01 import first_task, second_task
from tests.common import Task


@pytest.mark.y2017d01
class TestDay01:
    """ Набор тестов для задач 1-ого дня """

    DAY = 1

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['1122'], 3),
            (['1111'], 4),
            (['1234'], 0),
            (['91212129'], 9),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2017_file_loader):
        assert first_task(y2017_file_loader(self.DAY, Task.first)) == 1102

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['1212'], 6),
            (['1221'], 0),
            (['123425'], 4),
            (['123123'], 12),
            (['12131415'], 4),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2017_file_loader):
        assert second_task(y2017_file_loader(self.DAY, Task.second)) == 1102
