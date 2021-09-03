""" Day 02: Corruption Checksum """

import pytest
from advent_of_code.y2017.d02 import first_task, second_task
from tests.common import Task


@pytest.mark.y2017d02
class TestDay02:
    """ Набор тестов для задач 2-ого дня """

    DAY = 2

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['5 1 9 5', '7 5 3', '2 4 6 8'], 18),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2017_file_loader):
        assert first_task(y2017_file_loader(self.DAY, Task.first)) == 30994

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['5 9 2 8', '9 4 7 3', '3 8 6 5'], 9),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2017_file_loader):
        assert second_task(y2017_file_loader(self.DAY, Task.second)) == 233
