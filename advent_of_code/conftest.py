""" Общие фикстуры """

from functools import partial
from pathlib import Path
from typing import Iterator
import pytest
from advent_of_code.common import Task, DATA_DIR


def _file_loader(path: Path, day: int, task: Task) -> Iterator[str]:
    """ Возвращает входной набор данных для указанной задачи

    :param path:    Полный путь к директории с входными данными
    :param day:     Порядковый номер дня
    :param task:    Номер задачи
    :return:        Входной набор данных
    """

    file_name = path / f'd{day:02d}.{task.value}'
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            yield line


@pytest.fixture()
def y2015_file_loader():
    """ Возвращает входной набор данных для указанной задачи за 2015 год """
    return partial(_file_loader, DATA_DIR / 'y2015')


@pytest.fixture()
def y2016_file_loader():
    """ Возвращает входной набор данных для указанной задачи за 2016 год """
    return partial(_file_loader, DATA_DIR / 'y2016')


@pytest.fixture()
def y2017_file_loader():
    """ Возвращает входной набор данных для указанной задачи за 2017 год """
    return partial(_file_loader, DATA_DIR / 'y2017')


@pytest.fixture()
def y2018_file_loader():
    """ Возвращает входной набор данных для указанной задачи за 2018 год """
    return partial(_file_loader, DATA_DIR / 'y2018')


@pytest.fixture()
def y2019_file_loader():
    """ Возвращает входной набор данных для указанной задачи за 2019 год """
    return partial(_file_loader, DATA_DIR / 'y2019')


@pytest.fixture()
def y2020_file_loader():
    """ Возвращает входной набор данных для указанной задачи за 2020 год """
    return partial(_file_loader, DATA_DIR / 'y2020')


@pytest.fixture()
def y2021_file_loader():
    """ Возвращает входной набор данных для указанной задачи за 2021 год """
    return partial(_file_loader, DATA_DIR / 'y2021')


@pytest.fixture()
def y2022_file_loader():
    """ Возвращает входной набор данных для указанной задачи за 2022 год """
    return partial(_file_loader, DATA_DIR / 'y2022')
