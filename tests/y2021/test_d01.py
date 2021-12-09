""" Day 01: Sonar Sweep """

import pytest
from advent_of_code.y2021.d01 import first_task, second_task
from tests.consts import Task


@pytest.mark.y2021d01
class TestDay01:
    """ Набор тестов для задач 1-ого дня """

    DAY = 1

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['199', '200', '208', '210', '200', '207', '240', '269', '260', '263'], 7),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2021_file_loader):
        assert first_task(y2021_file_loader(self.DAY, Task.first)) == 1616

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['199', '200', '208', '210', '200', '207', '240', '269', '260', '263'], 5),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2021_file_loader):
        assert second_task(y2021_file_loader(self.DAY, Task.second)) == 1645
