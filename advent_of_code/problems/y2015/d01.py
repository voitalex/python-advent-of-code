""" Day 1: Not Quite Lisp

Link: https://adventofcode.com/2015/day/1

Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars,
and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar;
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor -
the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows
the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ),
means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example :
  * (()) and ()() both result in floor 0.
  * ((( and (()(()( both result in floor 3.
  * ))((((( also results in floor 3.
  * ()) and ))( both result in floor -1 (the first basement level).
  * ))) and )())()) both result in floor -3.

To what floor do the instructions take Santa?

------------------------------------------------------------------------------------------------------------------------
--- Part Two ---

Now, given the same instructions, find the position of the first character that causes him to enter
the basement (floor -1). The first character in the instructions has position 1, the second character
has position 2, and so on.

For example:
  * ) causes him to enter the basement at character position 1.
  * ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the basement?
"""

import itertools
from typing import Iterable


def _up_or_down(direction: str) -> int:
    """ Возвращает целочисленное смещение в зависимости от направления """
    return {
        '(': 1,
        ')': -1,
    }.get(direction, 0)


def first_task(instructions: Iterable[str]) -> int:
    """ Решение первой задачи """

    return sum(
        _up_or_down(direction)
        for direction in itertools.chain.from_iterable(instructions)
    )


def second_task(instructions: Iterable[str]) -> int:
    """ Решение второй задачи """

    def below_basement(value: int) -> bool:
        return value <= 0

    position: int = 1
    for index, instruction in enumerate(itertools.chain.from_iterable(instructions), start=1):
        position += _up_or_down(instruction)
        if below_basement(position):
            return index

    return 0
