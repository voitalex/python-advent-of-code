""" Вспомогательные утилиты """

from enum import unique, Enum
from itertools import starmap
from pathlib import Path
from typing import TypeVar


ChunkedElem = TypeVar('ChunkedElem')
FirstElem = TypeVar('FirstElem')
LastElem = TypeVar('LastElem')
TakeElem = TypeVar('TakeElem')
WindowedElem = TypeVar('WindowedElem')


BASE_DIR: Path = Path(__file__).parent
DATA_DIR: Path = BASE_DIR / 'data'


@unique
class Task(Enum):
    """ Идентификатор задачи в разрезе дня """
    first = 1
    second = 2


def zip_with(func, *args):
    """ Применение функции func для кортежа элементов из разных источников """
    return starmap(func, zip(*args))
