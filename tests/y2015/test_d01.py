""" Day 1: Not Quite Lisp """


import pytest
from advent_of_code.y2015.d01 import first_task, second_task
from tests.consts import Task


@pytest.mark.y2015d01
class TestDay01:
    """ Набор тестов для задач 1-ого дня """

    DAY = 1

    @pytest.mark.parametrize(
        'value, expected',
        [
            ('(())', 0),
            ('()()', 0),
            ('(((', 3),
            ('(()(()(', 3),
            ('))(((((', 3),
            ('())', -1),
            ('))(', -1),
            (')))', -3),
            (')())())', -3),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2015_file_loader):
        assert first_task(y2015_file_loader(self.DAY, Task.first)) == 74

    @pytest.mark.parametrize(
        'value, expected',
        [
            (')', 1),
            ('()())', 5),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2015_file_loader):
        assert second_task(y2015_file_loader(self.DAY, Task.second)) == 1795
