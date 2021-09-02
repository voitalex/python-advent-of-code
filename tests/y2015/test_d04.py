""" Day 4: The Ideal Stocking Stuffer """

import pytest
from advent_of_code.y2015.d04 import first_task, second_task


@pytest.mark.y2015d04
class TestDay04:
    """ Набор тестов для задач 4-ого дня """

    DAY = 4

    @pytest.mark.parametrize(
        'value, expected',
        [
            ('ckczppom', 117946),
        ]
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected

    @pytest.mark.skip
    @pytest.mark.parametrize(
        'value, expected',
        [
            ('ckczppom', 3938038),
        ]
    )
    def test_second_task_oneliners(self, value, expected):
        assert second_task(value) == expected
