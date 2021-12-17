""" Day 04: High-Entropy Passphrases """

import pytest
from advent_of_code.y2017.d04 import first_task, second_task
from tests.consts import Task


@pytest.mark.y2017d04
class TestDay04:
    """ Набор тестов для задач 4-ого дня """

    DAY = 4

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['aa bb cc dd ee'], 1),
            (['aa bb cc dd aa'], 0),
            (['aa bb cc dd aaa'], 1),
            (['imyql xotcl poql rlueapq bkwykm hlalk bkwykm'], 0)
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    def test_first_task_from_file(self, y2017_file_loader):
        assert first_task(y2017_file_loader(self.DAY, Task.first)) == 466

    @pytest.mark.parametrize(
        'value, expected',
        [
            (['abcde fghij'], 1),
            (['abcde xyz ecdab'], 0),
            (['a ab abc abd abf abj'], 1),
            (['iiii oiii ooii oooi oooo'], 1),
            (['oiii ioii iioi iiio'], 0),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected

    def test_second_task_from_file(self, y2017_file_loader):
        assert second_task(y2017_file_loader(self.DAY, Task.first)) == 251
