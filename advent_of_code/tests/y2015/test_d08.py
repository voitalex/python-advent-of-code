""" Day 8: Matchsticks """

import pytest
from advent_of_code.common import Task
from advent_of_code.problems.y2015.d08 import first_task, second_task


@pytest.mark.y2015d08
class TestDay08:
    """ Набор тестов для задач 8-ого дня """

    DAY = 8

    @pytest.mark.parametrize(
        'value, expected',
        [
            (
                [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'],
                12,
            ),
        ],
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2015_file_loader):
        assert first_task(y2015_file_loader(self.DAY, Task.first)) == 1333

    @pytest.mark.parametrize(
        'value, expected',
        [
            (
                [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'],
                19,
            ),
        ],
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2015_file_loader):
        assert second_task(y2015_file_loader(self.DAY, Task.first)) == 2046
