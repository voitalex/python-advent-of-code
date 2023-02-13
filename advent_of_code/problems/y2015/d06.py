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
import itertools
import re
from dataclasses import dataclass
from enum import unique, Enum, IntEnum
from typing import Iterable, Iterator, Callable, Optional

# Максимальный размер гирлянды с лампочками
MAX_GRID_SIZE = 1000


@unique
class Action(Enum):
    """ Действие с лампочкой """
    on = 'on'
    off = 'off'
    toggle = 'toggle'


@dataclass(frozen=True)
class Point:
    """ Координата на плоскости """
    x: int
    y: int


@dataclass(frozen=True)
class Range:
    """ Диапазон точек на плоскости """

    top: Point
    bottom: Point

    def __iter__(self) -> Iterator[Point]:
        """ Возвращает точки из диапазона точек """
        for y in range(self.top.y, self.bottom.y + 1):
            for x in range(self.top.x, self.bottom.x + 1):
                yield Point(x, y)


@dataclass(frozen=True)
class Command:
    """ Входная команда на изменение состояния лампочек """
    action: Action
    range: Range


@dataclass(frozen=True)
class Light:
    """ Лампочка """
    brightness: int
    location: Point


class Garland:
    """ Гирлянда из лампочек """

    def __init__(self, grid_size: int, def_brightness: int = 0) -> None:
        self.grid_size: int = grid_size
        self.garland_range: Range = Range(top=Point(0, 0), bottom=Point(grid_size - 1, grid_size - 1))
        self.garland: array.array = array.array('i', itertools.repeat(def_brightness, grid_size * grid_size))

    def _get_light_brightness(self, point: Point) -> int:
        """ Возвращает состояние (яркость) лампочки исходя из двумерных координат """
        return self.garland[self._calc_offset(point)]

    def _calc_offset(self, point: Point) -> int:
        """ Возвращает положение лампочки исходя из двумерных координат """
        return point.y * self.grid_size + point.x

    def _set_light_brightness(self, point: Point, value: int) -> None:
        """ Обновляет состояние лампочки """
        self.garland[self._calc_offset(point)] = value

    def apply(self, cmd: Command, calculate_light_brightness: Callable[[Action, Light], int]) -> None:
        """ Применение команды """
        for light in self.iterate(cmd.range):
            self._set_light_brightness(
                point=light.location,
                value=calculate_light_brightness(cmd.action, light),
            )

    def iterate(self, range: Optional[Range] = None) -> Iterable[Light]:
        """ Возвращает последовательность лампочек в указанном диапазоне """
        range = range or self.garland_range
        for point in range:
            yield Light(
                brightness=self._get_light_brightness(point),
                location=point,
            )

    def count(self, brightness: int) -> int:
        """ Возвращает количество лампочек с указанной яркостью """
        return len([x for x in self.garland if x == brightness])


def _parse_input(commands: Iterable[str]) -> Iterator[Command]:
    """ Возвращает команду для вкл/выкл лампочек исходя из строкового представления """

    template = re.compile(r'(on|off|toggle).*?(\d+),(\d+).*?(\d+),(\d+)')
    for str_command in commands:
        if res := re.search(template, str_command):
            yield Command(
                action=Action(res.group(1)),
                range=Range(
                    top=Point(int(res.group(2)), int(res.group(3))),
                    bottom=Point(int(res.group(4)), int(res.group(5))),
                )
            )


def first_task(commands: Iterable[str]) -> int:
    """ Решение первой задачи """

    @unique
    class Light(IntEnum):
        """ Дискретные значения яркости лампочки """
        off = 0
        on = 1

    def calculate_light_brightness(action: Action, light: Light) -> int:
        """ Расчет яркости лампочки """
        return {
            action.on: Light.on.value,
            action.off: Light.off.value,
            action.toggle: abs(Light.on.value - light.brightness),
        }[action]

    garland = Garland(MAX_GRID_SIZE)

    for command in _parse_input(commands):
        garland.apply(command, calculate_light_brightness)

    return len([x for x in garland.iterate() if x.brightness == Light.on.value])


def second_task(commands: Iterable[str]) -> int:
    """ Решение второй задачи """

    @unique
    class Light(IntEnum):
        """ Дискретные значения яркости лампочки """
        off = -1
        on = 1
        toggle = 2

    def calculate_light_brightness(action: Action, light: Light) -> int:
        """ Расчет яркости лампочки """
        brightness_change = {
            action.on: Light.on.value,
            action.off: Light.off.value,
            action.toggle: Light.toggle.value,
        }
        return max(0, light.brightness + brightness_change[action])

    garland = Garland(MAX_GRID_SIZE)
    for command in _parse_input(commands):
        garland.apply(command, calculate_light_brightness)

    return sum(x.brightness for x in garland.iterate())
