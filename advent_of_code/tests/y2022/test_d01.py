""" Day 01: Calorie Counting """

import pytest
from advent_of_code.common import Task
from advent_of_code.problems.y2022.d01 import first_task, second_task


@pytest.mark.y2022d01
class TestDay01:
    """ Набор тестов для задач 1-ого дня """

    DAY = 1

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000'], 24000),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2022_file_loader):
        assert first_task(y2022_file_loader(self.DAY, Task.first)) == 71506

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000'], 45000),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2022_file_loader):
        assert second_task(y2022_file_loader(self.DAY, Task.first)) == 209603
