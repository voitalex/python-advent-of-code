""" Day 5: Doesn't He Have Intern-Elves For This? """

import pytest
from advent_of_code.y2015.d05 import first_task, second_task
from tests.common import Task


@pytest.mark.y2015d05
class TestDay05:
    """ Набор тестов для задач 5-ого дня """

    DAY = 5

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['ugknbfddgicrmopn'], 1),
            (['jchzalrnumimnmhp'], 0),
            (['haegwjzuvuyypxyu'], 0),
            (['dvszwmarrgswjxmb'], 0),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2015_file_loader):
        assert first_task(y2015_file_loader(self.DAY, Task.first)) == 255

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['qjhvhtzxzqqjkmpb'], 1),
            (['xxyxx'], 1),
            (['uurcxstgmygtbstg'], 0),
            (['ieodomkazucvgmuy'], 0),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2015_file_loader):
        assert second_task(y2015_file_loader(self.DAY, Task.second)) == 55
