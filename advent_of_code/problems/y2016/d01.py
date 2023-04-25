""" Day 1: No Time for a Taxicab

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately,
is as close as you can get - the instructions on the Easter Bunny Recruiting Document
the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed)
and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees,
then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment
and work out the destination. Given that you can only walk on the street grid of the city,
how far is the shortest path to the destination?

For example:

  * Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
  * R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
  * R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?

------------------------------------------------------------------------------------------------------------------------
--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document.
Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location
you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""

from dataclasses import dataclass
from enum import Enum, unique
from typing import Iterable, Iterator, List, Optional


@unique
class Direction(Enum):
    """ Направление движения """
    north = 'north'
    east = 'east'
    south = 'south'
    west = 'west'


@unique
class Orientation(Enum):
    """ Ориентация интервала """
    horizontal = 'horizontal'
    vertical = 'vertical'


@unique
class Turn(Enum):
    """ Направление поворота """
    left = 'L'
    right = 'R'


@dataclass(frozen=True)
class Command:
    """ Команда для продвижения по городу """
    turn: Turn
    blocks: int


@dataclass(frozen=True)
class Point:
    """ Точка на карте """
    x: int
    y: int

    @property
    def distance(self) -> int:
        """ Возвращает расстояние от начала координат до текущего местоположения """
        return abs(self.x) + abs(self.y)


class Interval:
    """ Интервал кварталов между двумя точками """

    def __init__(self, start: Point, finish: Point) -> None:

        self.orientation = Orientation.horizontal if start.y == finish.y else Orientation.vertical

        if self.orientation == Orientation.horizontal:
            self.start, self.finish = (start, finish) if start.x <= finish.x else (finish, start)
        else:
            self.start, self.finish = (start, finish) if start.y <= finish.y else (finish, start)

    def __str__(self) -> str:
        """ Возвращает строковое представление объекта """
        return f'start={self.start} finish={self.finish}'


@dataclass(frozen=True)
class Position:
    """ Расположение и ориентация на карте """
    point: Point
    direction: Direction


def _generate_commands(strings: Iterable[str]) -> Iterator[Command]:
    """ Генерация команд на лету """

    def _parse(value: str) -> Command:
        """ Возвращает команду для продвижения по городу, сформированную из строкового представления """
        turn, *blocks = value
        return Command(turn=Turn(turn), blocks=int(''.join(blocks)))

    for string in strings:
        yield from map(_parse, string.split(', '))


def _move(current: Position, command: Command) -> Position:
    """ Возвращает обновленные координаты положения исходя из текущего положения и команды """

    direction: Direction = {
        Turn.left: {
            Direction.north: Direction.west,
            Direction.east: Direction.north,
            Direction.south: Direction.east,
            Direction.west: Direction.south,
        },
        Turn.right: {
            Direction.north: Direction.east,
            Direction.east: Direction.south,
            Direction.south: Direction.west,
            Direction.west: Direction.north,
        },
    }[command.turn][current.direction]

    dx, dy = {
        Direction.north: (0, 1),
        Direction.east: (1, 0),
        Direction.south: (0, -1),
        Direction.west: (-1, 0),
    }[direction]

    return Position(
        direction=direction,
        point=Point(
            x=current.point.x + dx * command.blocks,
            y=current.point.y + dy * command.blocks,
        )
    )


def first_task(strings: Iterable[str]) -> int:
    """ Решение первой задачи """

    current_position = Position(point=Point(x=0, y=0), direction=Direction.north)
    for command in _generate_commands(strings):
        current_position = _move(current=current_position, command=command)

    return current_position.point.distance


def second_task(strings: Iterable[str]) -> int:
    """ Решение второй задачи """

    def interval_intersection(first: Interval, second: Interval) -> Optional[Point]:
        """ Возвращает точку пересечения интервалов """

        if first.orientation == second.orientation:
            return None

        if first.orientation == Orientation.horizontal:
            if first.start.x < second.start.x < first.finish.x and second.start.y < first.start.y < second.finish.y:
                return Point(x=second.start.x, y=first.start.y)

        if first.orientation == Orientation.vertical:
            if second.start.x < first.start.x < second.finish.x and first.start.y < second.start.y < first.finish.y:
                return Point(x=first.start.x, y=second.start.y)

        return None

    prev_intervals: List[Interval] = []
    current_position = Position(point=Point(x=0, y=0), direction=Direction.north)

    for command in _generate_commands(strings):
        new_position = _move(current=current_position, command=command)
        interval = Interval(start=current_position.point, finish=new_position.point)

        for prev_interval in prev_intervals:
            intersection_point = interval_intersection(first=prev_interval, second=interval)
            if intersection_point is not None:
                return intersection_point.distance

        prev_intervals.append(interval)
        current_position = new_position

    return 0
