""" Day 04: Giant Squid """

from collections import defaultdict
from itertools import chain
from typing import Iterable, List, FrozenSet, Dict, Tuple
from advent_of_code.common import first, chunked, last


class Board:
    """ Игровое поле """

    def __init__(self, index: int, numbers: Iterable[str]) -> None:
        self.index = index
        self._grid, self._row_sums, self._column_sums = self._create_grid(numbers)

    @property
    def available_numbers(self) -> FrozenSet[int]:
        """ Возвращает оставшиеся номера на игровом поле """
        return frozenset(self._grid.keys())

    @property
    def winner(self) -> bool:
        """ Возвращает True если вычеркнуты все номера в строке или столбце """
        return any(not value for value in chain(self._row_sums, self._column_sums))

    def mark(self, number: int) -> None:
        """ Вычеркивает выпавший номер с игровой доски """

        if number not in self._grid:
            return

        row, column = self._grid.pop(number)
        print(f'Number: {number}. Found in board {self.index}')

        self._refresh_sums(row, column, number)

    def _refresh_sums(self, row: int, column: int, number: int):
        """ Актуализация сумм по строкам по оставшимся цифрам """
        self._row_sums[row] -= number
        self._column_sums[column] -= number

    @staticmethod
    def _create_grid(lines: Iterable[str]) -> Tuple[Dict[int, Tuple[int, int]], List[int], List[int]]:
        """ Создание игрового поля """

        grid = {}
        row_sums = defaultdict(int)
        column_sums = defaultdict(int)
        for row, line in enumerate(lines):
            for column, value in enumerate(int(x) for x in line.split(' ') if x):
                grid[value] = (row, column)
                row_sums[row] += value
                column_sums[column] += value

        row_sums = [row_sums[key] for key in sorted(row_sums)]
        column_sums = [column_sums[key] for key in sorted(column_sums)]

        return grid, row_sums, column_sums


class BoardSet:
    """ Набор игровых полей """

    _boards: List[Board]

    def __init__(self, line_size: int, numbers: Iterable[str]) -> None:
        self._boards: List[Board] = [Board(index, values) for index, values in enumerate(chunked(line_size, numbers))]
        self._winner_boards = set()

    def available_numbers(self, index: int) -> FrozenSet[int]:
        """ Возвращает множество оставшихся номером на указанном игровом поле """
        return self._boards[index].available_numbers

    @property
    def boards(self) -> int:
        """ Возвращает количество игровых полей """
        return len(self._boards)

    def mark(self, number: int) -> List[int]:
        """ Возвращает список выигравших игровых полей после вычеркивания указанного номера """

        current_winner_boards = []
        available_boards = (board for board in self._boards if board.index not in self._winner_boards)
        for board in available_boards:
            board.mark(number)
            if board.winner:
                current_winner_boards.append(board.index)

        self._winner_boards.update(current_winner_boards)

        return current_winner_boards


def first_task(strings: Iterable[str]):
    """
    You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't
    see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside
    of your submarine.

    Maybe it wants to play bingo?

    Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random,
    and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.)
    If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

    The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time.
    It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input).
    For example: 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

        22 13 17 11  0
         8  2 23  4 24
        21  9 14 16  7
         6 10  3 18  5
         1 12 20 15 19

         3 15  0  2 22
         9 18 13 17  5
        19  8  7 25 23
        20 11 10 24  4
        14 21 16 12  6

        14 21 17 24  4
        10 16 15  9 19
        18  8 23 26 20
        22 11 13  6  5
         2  0 12  3  7

    After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked
    as follows (shown here adjacent to each other to save space):

        22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
         8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
        21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
         6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
         1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

    After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

        22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
         8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
        21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
         6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
         1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

    Finally, 24 is drawn:

        22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
         8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
        21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
         6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
         1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

    At this point, the third board wins because it has at least one complete row or column of marked numbers
    (in this case, the entire top row is marked: 14 21 17 24 4).

    The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on
    that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when
    the board won, 24, to get the final score, 188 * 24 = 4512.

    To guarantee victory against the giant squid, figure out which board will win first. What will your final score
    be if you choose that board?
    """

    strings = (string for string in strings if string and string.strip())
    raw_numbers = first(strings)
    numbers = [int(value) for value in raw_numbers.split(',')]
    board_set = BoardSet(line_size=5, numbers=strings)

    for number in numbers:
        winner = first(board_set.mark(number))
        if winner is not None:
            return number * sum(board_set.available_numbers(winner))

    return 0


def second_task(strings: Iterable[str]) -> int:
    """
    On the other hand, it might be wise to try a different strategy: let the giant squid win.

    You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting
    its arms, the safe thing to do is to figure out which board will win last and choose that one. That way,
    no matter which boards it picks, it will win for sure.

    In the above example, the second board is the last to win, which happens after 13 is eventually called and
    its middle column is completely marked. If you were to keep playing until this point, the second board would
    have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

    Figure out which board will win last. Once it wins, what would its final score be?
    """

    strings = (string for string in strings if string and string.strip())
    raw_numbers = first(strings)
    numbers = [int(value) for value in raw_numbers.split(',')]
    board_set = BoardSet(line_size=5, numbers=strings)

    winning_score = 0
    for number in numbers:
        winner = last(board_set.mark(number))
        winning_score = number * sum(board_set.available_numbers(winner)) if winner else winning_score

    return winning_score
