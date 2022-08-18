""" Day 7: Some Assembly Required """

import pytest
from advent_of_code.common import Task
from advent_of_code.problems.y2015.d07 import first_task


@pytest.mark.y2015d07
class TestDay07:
    """ Набор тестов для задач 7-ого дня """

    DAY = 7

    @pytest.mark.parametrize(
        "value, expected",
        [
            (
                [
                    "123 -> xy",
                    "456 -> y",
                    "xy AND y -> a",
                    "xy OR y -> e",
                    "xy LSHIFT 2 -> f",
                    "y RSHIFT 2 -> g",
                    "NOT x -> h",
                    "NOT y -> i",
                ],
                72,
            ),
        ],
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2015_file_loader):
        assert first_task(y2015_file_loader(self.DAY, Task.first)) == 956
