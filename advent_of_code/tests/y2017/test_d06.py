""" Day 06: Memory Reallocation """

import pytest
from advent_of_code.common import Task
from advent_of_code.problems.y2017.d06 import first_task


@pytest.mark.y2017d06
class TestDay06:
    """ Набор тестов для задач 5-ого дня """

    DAY = 6

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
