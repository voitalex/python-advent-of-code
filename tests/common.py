""" Константы и функции общего назначения """

from enum import unique, Enum
from pathlib import Path


BASE_DIR: Path = Path(__file__).parent.parent
DATA_DIR: Path = BASE_DIR / 'data'


@unique
class Task(Enum):
    """ Порядковый номер задачи в течение дня """
    first = 1
    second = 2
