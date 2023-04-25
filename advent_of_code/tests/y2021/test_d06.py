""" Day 06: Lanternfish """

import pytest
from advent_of_code.common import Task
from advent_of_code.problems.y2021.d06 import first_task, second_task


@pytest.mark.y2021d06
class TestDay06:
    """ Набор тестов для задач 6-ого дня """

    DAY = 6

    @pytest.mark.parametrize(
        'days, fish_school, expected',
        [(18, ['3,4,3,1,2'], 26)]
    )
    def test_first_task_oneliners(self, days, fish_school, expected):
        assert first_task(days, fish_school) == expected

    def test_first_task_from_file(self, y2021_file_loader):
        assert first_task(80, y2021_file_loader(self.DAY, Task.first)) == 391888

    @pytest.mark.parametrize(
        'days, fish_school, expected',
        [(256, ['3,4,3,1,2'], 26984457539)]
    )
    def test_second_task_oneliners(self, days, fish_school, expected):
        assert second_task(days, fish_school) == expected

    def test_second_task_from_file(self, y2021_file_loader):
        assert first_task(256, y2021_file_loader(self.DAY, Task.first)) == 1754597645339
