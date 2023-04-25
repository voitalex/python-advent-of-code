""" Day 2: Bathroom Security

You arrive at Easter Bunny Headquarters under cover of darkness. However, you left in such a rush
that you forgot to use the bathroom! Fancy office buildings like this one usually have keypad locks
on their bathrooms, so you search the front desk for the code.

"In order to improve security," the document you find says, "bathroom codes will no longer be written down.
Instead, please memorize and follow the procedure below to access the bathrooms."

The document goes on to explain that each button to be pressed can be found by starting on the previous
button and moving to adjacent buttons on the keypad: U moves up, D moves down, L moves left, and R moves right.
Each line of instructions corresponds to one button, starting at the previous button (or, for the first line,
the "5" button); press whatever button you're on at the end of each line. If a move doesn't lead to a button,
ignore it.

You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom.
You picture a keypad like this:
    1 2 3
    4 5 6
    7 8 9

Suppose your instructions are:
    ULL
    RRDDD
    LURDL
    UUUUD
You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"),
so the first button is 1. Starting from the previous button ("1"), you move right twice (to "3") and
then down three times (stopping at "9" after two moves and ignoring the third), ending up with 9. Continuing
from "9", you move left, up, right, down, and left, ending with 8. Finally, you move up four times
(stopping at "2"), then down once, ending with 5. So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front desk.
What is the bathroom code?

------------------------------------------------------------------------------------------------------------------------
--- Part Two ---


"""

from dataclasses import dataclass
from typing import Iterable

keypad_size = 3


@dataclass(frozen=True)
class Button:
    """ Кнопка на клавиатуре """

    x: int
    y: int

    @property
    def value(self) -> str:
        """ Возвращает значение кнопки """
        return str(keypad_size * self.y + (self.x + 1))


def _apply_command(command: str, current: Button) -> Button:
    """ Возвращает расположение кнопки на основе команды и текущего расположения """
    dx, dy = {
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0),
    }[command]

    new_x, new_y = current.x + dx, current.y + dy
    if 0 <= new_x < keypad_size and 0 <= new_y < keypad_size:
        return Button(new_x, new_y)

    return current


def _apply_commands(commands: str, start: Button) -> Button:
    """ Применение набора команд для поиска кнопки """
    result = start
    for command in commands:
        result = _apply_command(command=command, current=result)
    return result


def first_task(strings: Iterable[str]) -> str:
    """ Решение первой задачи """

    buttons = []
    start = Button(x=1, y=1)
    for commands in strings:
        button = start = _apply_commands(commands=commands, start=start)
        buttons.append(button)

    return "".join([x.value for x in buttons])
