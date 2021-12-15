""" Day 04: Giant Squid """

import pytest
from advent_of_code.y2021.d04 import first_task, second_task
from tests.consts import Task


@pytest.mark.y2021d04
class TestDay04:
    """ Набор тестов для задач 4-ого дня """

    DAY = 4

    @pytest.mark.parametrize(
        'values, expected',
        [
            (
                ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
                 '22 13 17 11 0',
                 '8 2 23  4 24',
                 '21 9 14 16 7',
                 '6 10 3 18 5',
                 '1 12 20 15 19',
                 ''
                 '3 15  0  2 22',
                 '9 18 13 17  5',
                 '19  8  7 25 23',
                 '20 11 10 24  4',
                 '14 21 16 12  6',
                 ''
                 '14 21 17 24  4',
                 '10 16 15  9 19',
                 '18  8 23 26 20',
                 '22 11 13  6  5',
                 '2  0 12  3  7'],
             4512),
        ]
    )
    def test_first_task_oneliners(self, values, expected):
        assert first_task(values) == expected

    def test_first_task_from_file(self, y2021_file_loader):
        assert first_task(y2021_file_loader(self.DAY, Task.first)) == 8442

    @pytest.mark.parametrize(
        'values, expected',
        [
            (
                ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
                 '22 13 17 11 0',
                 '8 2 23  4 24',
                 '21 9 14 16 7',
                 '6 10 3 18 5',
                 '1 12 20 15 19',
                 ''
                 '3 15  0  2 22',
                 '9 18 13 17  5',
                 '19  8  7 25 23',
                 '20 11 10 24  4',
                 '14 21 16 12  6',
                 ''
                 '14 21 17 24  4',
                 '10 16 15  9 19',
                 '18  8 23 26 20',
                 '22 11 13  6  5',
                 '2  0 12  3  7'],
             1924),
        ]
    )
    def test_second_task_oneliners(self, values, expected):
        assert second_task(values) == expected

    def test_second_task_from_file(self, y2021_file_loader):
        assert second_task(y2021_file_loader(self.DAY, Task.second)) == 4590
