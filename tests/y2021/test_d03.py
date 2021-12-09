""" Day 03: Binary Diagnostic """

import pytest
from advent_of_code.y2021.d03 import first_task, second_task
from tests.consts import Task


@pytest.mark.y2021d03
class TestDay03:
    """ Набор тестов для задач 3-ого дня """

    DAY = 3

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['00100',
              '11110',
              '10110',
              '10111',
              '10101',
              '01111',
              '00111',
              '11100',
              '10000',
              '11001',
              '00010',
              '01010'],
             198),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2021_file_loader):
        assert first_task(y2021_file_loader(self.DAY, Task.first)) == 1071734

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['00100',
              '11110',
              '10110',
              '10111',
              '10101',
              '01111',
              '00111',
              '11100',
              '10000',
              '11001',
              '00010',
              '01010'],
             230),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2021_file_loader):
        assert second_task(y2021_file_loader(self.DAY, Task.second)) == 6124992
