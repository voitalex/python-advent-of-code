""" Day 05: Hydrothermal Venture """

import typing
from collections import Counter
from dataclasses import dataclass
from enum import IntEnum, unique
from typing import Iterable, Tuple, Dict


Grid = Dict[Tuple[int, int], int]


@dataclass(frozen=True)
class Point:
    """ Координаты точки """
    x: int
    y: int

    def __str__(self) -> str:
        """ Возвращает координаты точки в виде строки """
        return f'({self.x}, {self.y})'


Points = Tuple[Point, ...]


@unique
class LineDirection(IntEnum):
    """ Направление линии """
    horizontal = 0
    vertical = 1
    diagonal_45 = 2
    other = 3


class Line:
    """ Координаты линии """

    start: Point
    finish: Point

    def __init__(self, start: Point, finish: Point) -> None:
        self.start: Point = start
        self.finish: Point = finish

    @classmethod
    def from_points(cls, start_x: int, start_y: int, finish_x: int, finish_y: int) -> 'Line':
        """ Создание линии на основе координат точек """
        return cls(Point(start_x, start_y), Point(finish_x, finish_y))

    @property
    def direction(self) -> LineDirection:
        """ Возвращает направление линии """

        if self.start.y == self.finish.y:
            return LineDirection.horizontal

        if self.start.x == self.finish.x:
            return LineDirection.vertical

        if abs(self.start.x - self.finish.x) == abs(self.start.y - self.finish.y):
            return LineDirection.diagonal_45

        return LineDirection.other

    def __str__(self) -> str:
        """ Возвращает координаты линии в виде строки """
        return f'{self.start} - {self.finish}'


def _generate_points(line: Line) -> Iterable[Point]:
    """ Разметка линии на пространственной сетке """

    x_offset = 1 if line.start.x < line.finish.x else -1
    y_offset = 1 if line.start.y < line.finish.y else -1

    if line.direction == LineDirection.horizontal:
        return (Point(x, line.start.y) for x in range(line.start.x, line.finish.x + x_offset, x_offset))

    if line.direction == LineDirection.vertical:
        return (Point(line.start.x, y) for y in range(line.start.y, line.finish.y + y_offset, y_offset))

    if line.direction == LineDirection.diagonal_45:
        xs = range(line.start.x, line.finish.x + x_offset, x_offset)
        ys = range(line.start.y, line.finish.y + y_offset, y_offset)
        return (Point(x, y) for x, y in zip(xs, ys))

    return ()


def _parse_input(strings: Iterable[str]) -> Iterable[Line]:
    """ Разбор входящих данных """

    coords = ((string.split(' -> ')) for string in strings)
    for start_coords, finish_coords in coords:
        start_x, start_y = (int(x) for x in start_coords.split(','))
        finish_x, finish_y = (int(x) for x in finish_coords.split(','))
        yield Line.from_points(start_x, start_y, finish_x, finish_y)


def first_task(strings: Iterable[str]):
    """
    You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large,
    opaque clouds, so it would be best to avoid them if possible.

    They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input)
    for you to review. For example:
        0,9 -> 5,9
        8,0 -> 0,8
        9,4 -> 3,4
        2,2 -> 2,1
        7,0 -> 7,4
        6,4 -> 2,0
        0,9 -> 2,9
        3,4 -> 1,4
        0,0 -> 8,8
        5,5 -> 8,2

    Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of
    one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points
    at both ends. In other words:

        An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
        An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

    For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

    So, the horizontal and vertical lines from the above list would produce the following diagram:

    .......1..
    ..1....1..
    ..1....1..
    .......1..
    .112111211
    ..........
    ..........
    ..........
    ..........
    222111....

    In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as
    the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s,
    for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9
    and 0,9 -> 2,9.

    To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap.
    In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

    Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
    """

    grid: typing.Counter[Point] = Counter()
    allow_line_directions = frozenset([LineDirection.horizontal, LineDirection.vertical])
    allowed_lines = (line for line in _parse_input(strings) if line.direction in allow_line_directions)

    for line in allowed_lines:
        grid.update(_generate_points(line))

    return len([frequency for frequency in grid.values() if frequency > 1])


def second_task(strings: Iterable[str]) -> int:
    """
    Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture;
    you need to also consider diagonal lines.

    Because of the limits of the hydrothermal vent mapping system, the lines in your list will only
    ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

     * An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
     * An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

    Considering all lines from the above example would now produce the following diagram:

        1.1....11.
        .111...2..
        ..2.1.111.
        ...1.2.2..
        .112313211
        ...1.2....
        ..1...1...
        .1.....1..
        1.......1.
        222111....

    You still need to determine the number of points where at least two lines overlap. In the above example,
    this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

    Consider all of the lines. At how many points do at least two lines overlap?
    """

    grid: typing.Counter[Point] = Counter()
    allow_line_directions = frozenset([LineDirection.horizontal, LineDirection.vertical, LineDirection.diagonal_45])
    allowed_lines = (line for line in _parse_input(strings) if line.direction in allow_line_directions)

    for line in allowed_lines:
        grid.update(_generate_points(line))

    return len([frequency for frequency in grid.values() if frequency > 1])
