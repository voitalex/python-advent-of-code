""" Вспомогательные утилиты """

from collections import deque
from collections.abc import Sequence
from itertools import starmap, islice, zip_longest
from typing import TypeVar, Tuple, Iterable, Optional, Deque


ChunkedElem = TypeVar('ChunkedElem')
FirstElem = TypeVar('FirstElem')
LastElem = TypeVar('LastElem')
TakeElem = TypeVar('TakeElem')
WindowedElem = TypeVar('WindowedElem')


def take(n: int, iterable: Iterable[TakeElem]) -> Tuple[TakeElem, ...]:
    """ Возвращает первые N элементов последовательности в качестве кортежа

        Реализация взята из проекта more-itertools.
    """
    return tuple(islice(iterable, n))


def chunked(
        n: int,
        iterable: Iterable[ChunkedElem],
        fill_value: Optional[ChunkedElem] = None
) -> Iterable[Tuple[ChunkedElem, ...]]:
    """ Возвращает разбиение последовательности на подпоследовательности указанной длины

        Реализация взята из проекта more-itertools.
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fill_value)


def first(iterable: Iterable[FirstElem]) -> Optional[FirstElem]:
    """ Возвращает первый элемент последовательности

    Возвращает None если последовательность не содержит элементов
    """
    return next(iter(iterable), None)


def last(iterable: Iterable[LastElem]) -> Optional[LastElem]:
    """ Возвращает последний элемент последовательности

    Возвращает None если последовательность не содержит элементов
    """

    try:
        if isinstance(iterable, Sequence):
            return iterable[-1]

        return deque(iterable, maxlen=1)[-1]

    except (IndexError, TypeError, StopIteration):
        return None


def windowed(iterable: Iterable[WindowedElem], length: int) -> Iterable[Tuple[WindowedElem, ...]]:
    """ Возвращает скользящее окно длины n из элементов последовательности.

        Реализация взята из проекта more-itertools.
    """

    window: Deque[WindowedElem] = deque(maxlen=length)
    i = length
    for _ in map(window.append, iterable):
        i -= 1
        if not i:
            i = 1
            yield tuple(window)


def zip_with(func, *args):
    """ Применение функции func для кортежа элементов из разных источников """
    return starmap(func, zip(*args))
