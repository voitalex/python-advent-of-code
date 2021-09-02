""" Day 3: Perfectly Spherical Houses in a Vacuum """

import pytest
from advent_of_code.y2015.d03 import first_task, second_task
from tests.common import Task


@pytest.mark.y2015d03
class TestDay03:
    """ Набор тестов для задач 3-ого дня """

    DAY = 3

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['>'], 2),
            (['^>v<'], 4),
            (['^v^v^v^v^v'], 2),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2015_file_loader):
        assert first_task(y2015_file_loader(self.DAY, Task.first)) == 2572

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['^v'], 3),
            (['^>v<'], 3),
            (['^v^v^v^v^v'], 11),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2015_file_loader):
        assert second_task(y2015_file_loader(self.DAY, Task.second)) == 2631
