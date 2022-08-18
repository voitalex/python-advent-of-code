""" Day 6: Probably a Fire Hazard

Because your neighbors keep defeating you in the holiday house decorating contest year after year,
you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on
how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are
at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle
various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners
of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights
in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions
Santa sent you in order.

For example:

  * turn on 0,0 through 999,999 would turn on (or leave on) every light.
  * toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones
    that were on, and turning on the ones that were off.
  * turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

------------------------------------------------------------------------------------------------------------------------
--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated
Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness
of zero or more. The lights all start at zero.

The phrase "turn on" actually means that you should increase the brightness of those lights by 1.

The phrase "turn off" actually means that you should decrease the brightness of those lights by 1,
to a minimum of zero.

The phrase "toggle" actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

  * turn on 0,0 through 0,0 would increase the total brightness by 1.
  * toggle 0,0 through 999,999 would increase the total brightness by 2000000.
"""

import array
import re
from dataclasses import dataclass
from typing import Iterable, Iterator

# Максимальный размер гирлянды с лампочками
MAX_GRID_SIZE = 1000


@dataclass(frozen=True)
class Command:
    """ Описание команды на включение лампочек """
    action: str
    top_x: int
    top_y: int
    bottom_x: int
    bottom_y: int


@dataclass(frozen=True)
class Instruction:
    """ Описание """
    action: str
    offset: int


def _parse_input(commands: Iterable[str]) -> Iterator[Command]:
    """ Возвращает команду для вкл/выкл лампочек исходя из строкового представления """

    template = re.compile(r'(on|off|toggle).*?(\d+),(\d+).*?(\d+),(\d+)')
    for str_command in commands:
        if res := re.search(template, str_command):
            yield Command(
                action=res.group(1),
                top_x=int(res.group(2)),
                top_y=int(res.group(3)),
                bottom_x=int(res.group(4)),
                bottom_y=int(res.group(5)),
            )


def _to_instructions(cmd: Command) -> Iterator[Instruction]:
    for y in range(cmd.top_y, cmd.bottom_y + 1):
        for x in range(cmd.top_x, cmd.bottom_x + 1):
            yield Instruction(action=cmd.action, offset=y * MAX_GRID_SIZE + x)


def first_task(commands: Iterable[str]) -> int:
    """ Решение первой задачи """

    lights = array.array('b', (0 for _ in range(MAX_GRID_SIZE * MAX_GRID_SIZE)))

    def apply_instruction(instruction: Instruction) -> None:
        if instruction.action == 'toggle':
            lights[instruction.offset] = abs(1 - lights[instruction.offset])
        else:
            lights[instruction.offset] = 1 if instruction.action == "on" else 0

    for command in _parse_input(commands):
        for instruction in _to_instructions(command):
            apply_instruction(instruction)

    return sum(lights)


def second_task(commands: Iterable[str]) -> int:
    """ Решение второй задачи """

    lights = array.array('b', (0 for _ in range(MAX_GRID_SIZE * MAX_GRID_SIZE)))

    def apply_instruction(instruction: Instruction) -> None:
        brightness_changes = {'on': 1, 'off': -1, 'toggle': 2}
        lights[instruction.offset] = max(0, lights[instruction.offset] + brightness_changes[instruction.action])

    for command in _parse_input(commands):
        for instruction in _to_instructions(command):
            apply_instruction(instruction)

    return sum(lights)
