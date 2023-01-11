""" Day 3: Perfectly Spherical Houses in a Vacuum

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at
the North Pole calls him via radio and tells him where to move next. Moves are always exactly
one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another
present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions
are a little off, and Santa ends up visiting some houses more than once. How many houses receive
at least one present?

For example:

  * > delivers presents to 2 houses: one at the starting location, and one to the east.
  * ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
  * ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

------------------------------------------------------------------------------------------------------------------------
--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver
presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house),
then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script
as the previous year.

This year, how many houses receive at least one present?

For example:

  * ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
  * ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
  * ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""

import itertools
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Position:
    """ Координаты дома """
    x: int
    y: int


def _move(position: Position, direction: str) -> Position:
    """ Возвращает координаты очередного дома с учетом шага и положения предыдущего дома """
    dx, dy = {
        '.': (0, 0),
        '^': (0, 1),
        '>': (1, 0),
        'v': (0, -1),
        '<': (-1, 0),
    }.get(direction, (0, 0))

    return Position(position.x + dx, position.y + dy)


def first_task(directions: Iterable[str]) -> int:
    """ Решение первой задачи """

    houses = set(
        itertools.accumulate(
            itertools.chain.from_iterable(directions),
            _move,
            initial=Position(x=0, y=0),
        )
    )

    return len(houses)


def second_task(directions: Iterable[str]) -> int:
    """ Решение второй задачи """

    santa_iter, robot_iter = itertools.tee(itertools.chain.from_iterable(directions))
    santa_directions = (direction for index, direction in enumerate(santa_iter) if index % 2 == 0)
    robot_directions = (direction for index, direction in enumerate(robot_iter) if index % 2 == 1)

    santa_houses = set(
        itertools.accumulate(
            santa_directions,
            _move,
            initial=Position(x=0, y=0),
        )
    )

    robot_houses = set(
        itertools.accumulate(
            robot_directions,
            _move,
            initial=Position(x=0, y=0),
        )
    )

    return len(santa_houses | robot_houses)
