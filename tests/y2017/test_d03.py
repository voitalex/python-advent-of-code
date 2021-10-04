""" Day 03: Spiral Memory """

import pytest
from advent_of_code.y2017.d03 import first_task, second_task


@pytest.mark.y2017d03
class TestDay03:
    """ Набор тестов для задач 3-ого дня """

    DAY = 3

    @pytest.mark.parametrize(
        'value, expected',
        [
            (1, 0),
            (12, 3),
            (23, 2),
            (1024, 31),
            (347991, 480),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    @pytest.mark.parametrize(
        'value, expected',
        [
            (1, 2),
            (4, 5),
            (11, 23),
            (23, 25),
            (347991, 349975),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected
