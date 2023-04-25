""" Day 02: Dive! """

import pytest
from advent_of_code.common import Task
from advent_of_code.problems.y2021.d02 import first_task, second_task


@pytest.mark.y2021d02
class TestDay02:
    """ Набор тестов для задач 2-ого дня """

    DAY = 2

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'], 150),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2021_file_loader):
        assert first_task(y2021_file_loader(self.DAY, Task.first)) == 2215080

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'], 900),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2021_file_loader):
        assert second_task(y2021_file_loader(self.DAY, Task.second)) == 1864715580
