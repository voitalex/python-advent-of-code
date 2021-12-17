""" Day 1: No Time for a Taxicab """


import pytest
from tests.consts import Task
from advent_of_code.y2016.d01 import first_task, second_task


@pytest.mark.y2016d01
class TestDay01:
    """ Набор тестов для задач 1-ого дня """

    DAY = 1

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['R2, L3'], 5),
            (['R2, R2, R2'], 2),
            (['R5, L5, R5, R3'], 12),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2016_file_loader):
        assert first_task(y2016_file_loader(self.DAY, Task.first)) == 161

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['R8, R4, R4, R8'], 4),
            (['R4, R4, R8, R8, R6, R8'], 2)
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2016_file_loader):
        assert second_task(y2016_file_loader(self.DAY, Task.second)) == 110
