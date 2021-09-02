""" Вспомогательные утилиты """

from itertools import starmap


def first(iterable):
    """ Возвращает первый элемент последовательности

    Возвращает None если последовательность не содержит элементов
    """
    return next(iter(iterable), None)


def zip_with(func, *args):
    """ Применение функции func для кортежа элементов из разных источников """
    return starmap(func, zip(*args))
