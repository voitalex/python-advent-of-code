""" Day 07: The Treachery of Whales """

import pytest
from advent_of_code.common import Task
from advent_of_code.problems.y2021.d07 import first_task, second_task


@pytest.mark.y2021d07
class TestDay07:
    """ Набор тестов для задач 7-ого дня """

    DAY = 7

    @pytest.mark.parametrize(
        'values, expected',
        [
            (['1,2'], 1),
            (['1,2,4'], 3),
            (['16,1,2,0,4,2,7,1,2,14'], 37),

        ]
    )
    def test_first_task_oneliners(self, values, expected):
        assert first_task(values) == expected

    def test_first_task_from_file(self, y2021_file_loader):
        assert first_task(y2021_file_loader(self.DAY, Task.first)) == 344605

    @pytest.mark.parametrize(
        'values, expected',
        [
            (['1,2'], 1),
            (['1,2,4'], 4),
            (['16,1,2,0,4,2,7,1,2,14'], 168),

        ]
    )
    def test_second_task_oneliners(self, values, expected):
        assert second_task(values) == expected

    def test_second_task_from_file(self, y2021_file_loader):
        assert second_task(y2021_file_loader(self.DAY, Task.second)) == 93699985
