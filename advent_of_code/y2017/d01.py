""" Day 01: Inverse Captcha """

import itertools
from typing import Iterable


def first_task(strings: Iterable[str]) -> int:
    """
    The night before Christmas, one of Santa's Elves calls you in a panic. "The printer's broken!
    We can't print the Naughty or Nice List!" By the time you make it to sub-basement 17, there are only
    a few minutes until midnight. "We have a big problem," she says; "there must be almost fifty bugs
    in this system, but nothing else can print The List. Stand in this square, quick! There's no time to explain;
    if you can convince them to pay you in stars, you'll be able to--" She pulls a lever and the world goes blurry.

    When your eyes can focus again, everything seems a lot more pixelated than before. She must have sent you
    inside the computer! You check the system clock: 25 milliseconds until midnight. With that much time,
    you should be able to collect all fifty stars by December 25th.

    Collect stars by solving puzzles. Two puzzles will be made available on each day millisecond in
    the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants
    one star. Good luck!

    You're standing in a room with "digitization quarantine" written in LEDs along one wall. The only door
    is locked, but it includes a small interface. "Restricted Area - Strictly No Digitized Users Allowed."

    It goes on to explain that you may only leave by solving a captcha to prove you're not a human.
    Apparently, you only get one millisecond to solve the captcha: too fast for a normal human,
    but it feels like hours to you.

    The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits
    that match the next digit in the list. The list is circular, so the digit after the last digit is the first
    digit in the list.

For example:

    * 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit
         and the third digit (2) matches the fourth digit.
    * 1111 produces 4 because each digit (all 1) matches the next.
    * 1234 produces 0 because no digit matches the next.
    * 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

    What is the solution to your captcha?
"""

    digits = [int(digit) for digit in itertools.chain.from_iterable(strings)]

    # Разбиение последовательности цифр на группы по две цифры
    pairs = zip(digits, digits[1:] + digits[:1])

    # Подсчет результата
    return sum(fst for fst, snd in pairs if fst == snd)


def second_task(strings: Iterable[str]) -> int:
    """
    You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied,
    but it did emit a star as encouragement. The instructions change:

        Now, instead of considering the next digit, it wants you to consider the digit halfway around
        the circular list. That is, if your list contains 10 items, only include a digit in your sum
        if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

    For example:

      * 1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
      * 1221 produces 0, because every comparison is between a 1 and a 2.
      * 123425 produces 4, because both 2s match each other, but no other digit has a match.
      * 123123 produces 12.
      * 12131415 produces 4.
    """

    result = 0
    digits = [int(digit) for digit in itertools.chain.from_iterable(strings)]
    halfway_around = len(digits) // 2

    for index, digit in enumerate(digits):
        if digit == digits[(index + halfway_around) % len(digits)]:
            result += digit

    return result