""" Day 03: Spiral Memory

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.
Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and
then counting up while spiraling outward. For example, the first few squares are allocated like this:

    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23 ---> ...

While this is very space-efficient (no squares are skipped), requested data must be carried back to
square 1 (the location of the only access port for this memory system) by programs that can only move
up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location
of the data and square 1.

For example:

  * Data from square 1 is carried 0 steps, since it's at the access port.
  * Data from square 12 is carried 3 steps, such as: down, left, left.
  * Data from square 23 is carried only 2 steps: up twice.
  * Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in your puzzle input all the way
to the access port?

------------------------------------------------------------------------------------------------------------------------
--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1.
Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares,
including diagonals.

So, the first few squares' values are chosen as follows:

  * Square 1 starts with the value 1.
  * Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
  * Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
  * Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
  * Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
  * Once a square is written, its value does not change. Therefore, the first few squares would receive
    the following values:

    147  142  133  122   59
    304    5    4    2   57
    330   10    1    1   54
    351   11   23   25   26
    362  747  806  --->  ...

What is the first value written that is larger than your puzzle input?
"""

from dataclasses import dataclass
from enum import unique, Enum
from typing import Dict, Callable, Iterable, Optional, Tuple


@unique
class Direction(Enum):
    """ Направление движения """
    east = (1, 0)
    north = (0, 1)
    west = (-1, 0)
    south = (0, -1)


@dataclass(frozen=True)
class Point:
    """ Координаты ячейки в таблице """
    x: int
    y: int


# Таблица в виде спирали
Table = Dict[Point, int]


def points() -> Iterable[Point]:
    """ Возвращает набор посещаемых точек исходя шага спирали и текущего положения

    Алгоритм генерации точек по спирали состоит из следующих шагов:
        Размер шага (N) равен 2
        Пока не выполняется условие по остановке обхода:
          Один шаг на восток
          N-1 шагов на север
          N шагов на запад
          N шагов на юг
          N шагов на восток
          N увеличиваем на 2
    """

    start_point = Point(x=0, y=0)
    yield start_point

    move_size = 2

    while True:

        direction_moves = (
            (Direction.east, 1),
            (Direction.north, move_size - 1),
            (Direction.west, move_size),
            (Direction.south, move_size),
            (Direction.east, move_size),
        )

        for direction, moves in direction_moves:

            dx, dy = direction.value
            current_point = start_point
            for _ in range(moves):
                current_point = Point(x=current_point.x + dx, y=current_point.y + dy)
                yield current_point

            start_point = current_point

        move_size += 2


def traverse_table(
        create_cell_value: Callable[[Table, Optional[Point], Point], int],
        stop_traversal: Callable[[Table, Point], bool],
) -> Tuple[Point, int]:
    """ Обход таблицы """

    table: Table = {}
    prev_point: Optional[Point] = None

    while True:

        for curr_point in points():
            table[curr_point] = create_cell_value(table, prev_point, curr_point)
            prev_point = curr_point
            if stop_traversal(table, curr_point):
                return curr_point, table[curr_point]


def first_task(value: int) -> int:
    """ Решение первой задачи """

    def create_cell_value(table: Table, prev_point: Optional[Point], _: Point) -> int:
        """ Алгоритм вычисления текущего значения в ячейке таблицы """

        if not prev_point:
            return 1

        return table[prev_point] + 1

    def stop_traversal(table: Table, curr_point: Point) -> bool:
        """ Алгоритм продолжения обхода таблицы по спирали """
        return table[curr_point] >= value

    point, _ = traverse_table(
        create_cell_value=create_cell_value,
        stop_traversal=stop_traversal,
    )

    return abs(point.x) + abs(point.y)


def second_task(value: int) -> int:
    """ Решение второй задачи """

    def create_cell_value(table: Table, prev_point: Optional[Point], curr_point: Point) -> int:
        """ Алгоритм вычисления текущего значения в ячейке таблицы """

        if not prev_point:
            return 1

        neighbour_points = [
            Point(x=curr_point.x + dx, y=curr_point.y + dy)
            for dx, dy in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        ]

        return sum(table.get(point, 0) for point in neighbour_points)

    def stop_traversal(table: Table, curr_point: Point) -> bool:
        """ Алгоритм продолжения обхода таблицы по спирали """
        return table[curr_point] > value

    _, value = traverse_table(
        create_cell_value=create_cell_value,
        stop_traversal=stop_traversal,
    )

    return value
