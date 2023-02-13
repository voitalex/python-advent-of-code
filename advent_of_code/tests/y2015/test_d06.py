""" Day 6: Probably a Fire Hazard """

import pytest
from advent_of_code.common import Task
from advent_of_code.problems.y2015.d06 import first_task, second_task


@pytest.mark.y2015d06
class TestDay06:
    """Набор тестов для задач 6-ого дня"""

    DAY = 6

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['turn on 0,0 through 999,999', 'toggle 0,0 through 999,0', 'turn off 499,499 through 500,500'], 998996),
        ],
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    @pytest.mark.skip
    def test_first_task_from_file(self, y2015_file_loader):
        assert first_task(y2015_file_loader(self.DAY, Task.first)) == 377891

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['turn on 0,0 through 0,0', 'toggle 0,0 through 999,999'], 2000001),
        ],
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    @pytest.mark.skip
    def test_second_task_from_file(self, y2015_file_loader):
        assert second_task(y2015_file_loader(self.DAY, Task.second)) == 14110788
