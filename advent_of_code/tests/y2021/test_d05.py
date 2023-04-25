""" Day 05: Hydrothermal Venture """

import pytest
from advent_of_code.common import Task
from advent_of_code.problems.y2021.d05 import first_task, second_task


@pytest.mark.y2021d05
class TestDay05:
    """ Набор тестов для задач 5-ого дня """

    DAY = 5

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['0,9 -> 5,9',
              '8,0 -> 0,8',
              '9,4 -> 3,4',
              '2,2 -> 2,1',
              '7,0 -> 7,4',
              '6,4 -> 2,0',
              '0,9 -> 2,9',
              '3,4 -> 1,4',
              '0,0 -> 8,8',
              '5,5 -> 8,2'],
             5),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2021_file_loader):
        assert first_task(y2021_file_loader(self.DAY, Task.first)) == 3990

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['0,9 -> 5,9',
              '8,0 -> 0,8',
              '9,4 -> 3,4',
              '2,2 -> 2,1',
              '7,0 -> 7,4',
              '6,4 -> 2,0',
              '0,9 -> 2,9',
              '3,4 -> 1,4',
              '0,0 -> 8,8',
              '5,5 -> 8,2'],
             12),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2021_file_loader):
        assert second_task(y2021_file_loader(self.DAY, Task.second)) == 21305
