
import pytest as pytest
from advent_of_code.common import chunked, take, windowed


@pytest.mark.parametrize(
    'n, iterable, expected',
    [
        (0, [], ()),
        (5, [], ()),
        (1, [1, 2, 3, 4, 5, 6], [(1,), (2,), (3,), (4,), (5,), (6,)]),
        (2, [1, 2, 3, 4, 5, 6], [(1, 2), (3, 4), (5, 6)]),
        (4, [1, 2, 3, 4, 5, 6], [(1, 2, 3, 4), (5, 6)]),
        (8, [1, 2, 3, 4, 5, 6], [(1, 2, 3, 4, 5, 6)]),
        (0, [1, 2, 3, 4, 5, 6], [()]),
    ],
)
def test_chunked(n, iterable, expected):
    assert list(chunked(n, iterable)) == list(expected)


@pytest.mark.parametrize(
    'n, iterable, expected',
    [
        (0, [], ()),
        (5, [], ()),
        (1, [1, 2, 3, 4, 5, 6], (1,)),
        (2, [1, 2, 3, 4, 5, 6], (1, 2)),
        (8, [1, 2, 3, 4, 5, 6], (1, 2, 3, 4, 5, 6)),
        (0, [1, 2, 3, 4, 5, 6], ()),
    ],
)
def test_take(n, iterable, expected):
    assert tuple(take(n, iterable)) == expected


@pytest.mark.parametrize(
    'iterable, length, expected',
    [
        ([1, 2, 3, 4, 5, 6], 2, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]),
        ([1, 2, 3, 4, 5, 6], 3, [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]),
    ],
)
def test_windowed(iterable, length, expected):
    assert list(windowed(iterable, length)) == expected
