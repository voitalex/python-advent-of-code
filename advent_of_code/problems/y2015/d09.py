""" Day 9: All in a Single Night

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances
between every pair of locations. He can start and end at any two (different) locations he wants,
but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:
  * London to Dublin = 464
  * London to Belfast = 518
  * Dublin to Belfast = 141

The possible routes are therefore:
  Dublin -> London -> Belfast = 982
  London -> Dublin -> Belfast = 605
  London -> Belfast -> Dublin = 659
  Dublin -> Belfast -> London = 659
  Belfast -> Dublin -> London = 605
  Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

------------------------------------------------------------------------------------------------------------------------
--- Part Two ---
"""

import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable, Mapping, Tuple, Dict


@dataclass(frozen=True)
class Route:
    """ Маршрут """
    departure: str
    arrival: str
    length: int


def _parse_input(string: str) -> Route:
    """ Возвращает маршрут из строкового представления """

    template = r'(\w+) to (\w+) = (\w+)'
    if (match := re.match(template, string)) is not None:
        return Route(
            departure=match.group(1),
            arrival=match.group(2),
            length=int(match.group(3)),
        )

    raise ValueError(f'Wrong route: {string}')


def first_task(strings: Iterable[str]) -> int:
    """ Решение первой задачи """

    # Формирование списка маршрутов
    routes = [_parse_input(string) for string in strings]

    # Инициализация матрицы смежности
    adj = []
    for route in routes:

        adj.append()
        length = 0 if route.departure == route.arrival else route.length
        adj[(route.departure, route.arrival)] = length
        adj[(route.arrival, route.departure)] = length

    # Инициализация матрицы кратчайших расстояний
    distances: Dict[Tuple[str, str], int] = {}
    for outer in adj:
        for inner in adj:
            if outer == inner:
                distances[(outer, inner)] = 0




    return 0

print(
    first_task(
        [
            'London to Dublin = 464',
            'London to Belfast = 518',
            'Dublin to Belfast = 141',
        ],
    )
)
