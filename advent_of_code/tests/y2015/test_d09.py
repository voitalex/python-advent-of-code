""" Day 9: Matchsticks """

import pytest
from advent_of_code.common import Task
from advent_of_code.problems.y2015.d09 import first_task


@pytest.mark.y2015d09
class TestDay09:
    """ Набор тестов для задач 9-ого дня """

    DAY = 9

    @pytest.mark.parametrize(
        'value, expected',
        [
            (
                [
                    'London to Dublin = 464',
                    'London to Belfast = 518',
                    'Dublin to Belfast = 141',
                ],
                605,
            ),
        ],
    )
    def test_first_task_oneliners(self, value, expected):
        assert first_task(value) == expected
