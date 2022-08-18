""" Day 2: I Was Told There Would Be No Math """


import pytest

from advent_of_code.common import Task
from advent_of_code.problems.y2015.d02 import first_task, second_task



@pytest.mark.y2015d02
class TestDay02:
    """ Набор тестов для задач 2-ого дня """

    DAY = 2

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['2x3x4'], 58),
            (['1x1x10'], 43),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2015_file_loader):
        assert first_task(y2015_file_loader(self.DAY, Task.first)) == 1586300

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['2x3x4'], 34),
            (['1x1x10'], 14),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2015_file_loader):
        assert second_task(y2015_file_loader(self.DAY, Task.second)) == 3737498
