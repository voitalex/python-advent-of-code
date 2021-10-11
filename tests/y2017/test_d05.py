""" Day 05: A Maze of Twisty Trampolines, All Alike """

import pytest
from advent_of_code.y2017.d05 import first_task, second_task
from tests.common import Task


@pytest.mark.y2017d05
class TestDay05:
    """ Набор тестов для задач 5-ого дня """

    DAY = 5

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['0', '3', '0', '1', '-3'], 5),
            (['0', '0', '0', '2', '2'], 7)
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2017_file_loader):
        assert first_task(y2017_file_loader(self.DAY, Task.first)) == 394829

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['0', '3', '0', '1', '-3'], 10),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2017_file_loader):
        assert second_task(y2017_file_loader(self.DAY, Task.second)) == 31150702
