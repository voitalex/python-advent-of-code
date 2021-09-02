""" Day 4: The Ideal Stocking Stuffer """

import hashlib
import itertools


def _generate_hash(value: str) -> str:
    """ Возвращает сформированный MD5-хеш для указанной строки """
    return hashlib.md5(value.encode('utf-8')).hexdigest()


def first_task(secret: str) -> int:
    """ Day 4: The Ideal Stocking Stuffer

    Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all
    the economically forward-thinking little girls and boys.

    To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.
    The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number
    in decimal. To mine AdventCoins, you must find Santa the lowest positive number
    (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

    For example:
      * If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts
        with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
      * If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting
        with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
    """

    for num in itertools.count():
        if _generate_hash(secret + str(num)).startswith('00000'):
            return num

    return 0


def second_task(secret: str) -> int:
    """ Day 4: The Ideal Stocking Stuffer

    Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all
    the economically forward-thinking little girls and boys.

    To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least six zeroes.
    The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number
    in decimal. To mine AdventCoins, you must find Santa the lowest positive number
    (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
    """

    for num in itertools.count():
        if _generate_hash(secret + str(num)).startswith('000000'):
            return num

    return 0