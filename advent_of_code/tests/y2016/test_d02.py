""" Day 2: Bathroom Security """

import pytest
from advent_of_code.common import Task
from advent_of_code.problems.y2016.d02 import first_task


@pytest.mark.y2016d02
class TestDay01:
    """ Набор тестов для задач 2-ого дня """

    DAY = 1

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['ULL', 'RRDDD', 'LURDL', 'UUUUD'], '1985'),
        ],
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2016_file_loader):
        assert first_task(y2016_file_loader(self.DAY, Task.first)) == 161
