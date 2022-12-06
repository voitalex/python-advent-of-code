""" Day 01: Calorie Counting

Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver
presents on Christmas. For that, their favorite snack is a special type of star fruit that only grows deep
in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th.
Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see
along the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar;
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves'
expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of
their supplies. One important consideration is food - in particular, the number of Calories each Elf
is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc.
that they've brought with them, one item per line. Each Elf separates their own inventory from the previous
Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

    1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000

This list represents the Calories of the food carried by five Elves:
  * the first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
  * the second Elf is carrying one food item with 4000 Calories.
  * the third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
  * the fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
  * the fifth Elf is carrying one food item with 10000 Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know
how many Calories are being carried by the Elf carrying the most Calories. In the example above,
this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

from queue import PriorityQueue
from typing import Iterable, List


def _first_n(count: int, strings: Iterable[str]) -> List[int]:
    """ Возвращает первые N элементов с наибольшим количеством калорий """

    # Для получения максимального значения из очереди с приоритетами значения сохраняются со знаком "-"

    all_calories = PriorityQueue()
    elf_calories = 0
    for string in (strings or []):

        value = string.strip()
        if value:
            elf_calories += int(value)
        else:
            all_calories.put(-1 * elf_calories)
            elf_calories = 0

    # Обработка последней суммы калорий
    if elf_calories:
        all_calories.put(-1 * elf_calories)

    return [-1 * all_calories.get() for _ in range(count)]


def first_task(strings: Iterable[str]) -> int:
    """ Решение первой задачи """
    return sum(_first_n(1, strings))


def second_task(strings: Iterable[str]) -> int:
    """ Решение первой задачи """
    return sum(_first_n(3, strings))
