""" Day 5: Doesn't He Have Intern-Elves For This?

Santa needs help figuring out which strings in his text file are naughty or nice.
A nice string is one with all of the following properties:

  * It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
  * It contains at least one letter that appears twice in a row, like xx, abcdde (dd),
    or aabbccdd (aa, bb, cc, or dd).
  * It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

  * ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...),
    a double letter (...dd...), and none of the disallowed substrings.
  * aaa is nice because it has at least three vowels and a double letter, even though
    the letters used by different rules overlap.
  * jchzalrnumimnmhp is naughty because it has no double letter.
  * haegwjzuvuyypxyu is naughty because it contains the string xy.
  * dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

Realizing the error of his ways, Santa has switched to a better model of determining
whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

  * It contains a pair of any two letters that appears at least twice in the string
    without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).

  * It contains at least one letter which repeats with exactly one letter between them,
    like xyx, abcdefeghi (efe), or even aaa.

For example:

  * qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter
    that repeats with exactly one letter between them (zxz).

  * xxyxx is nice because it has a pair that appears twice and a letter that repeats
  with one between, even though the letters used by each rule overlap.

  * uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single
    letter between them.

  * ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo),
    but no pair that appears twice.

How many strings are nice under these new rules?
"""

import re
from typing import Iterable
from advent_of_code.common import zip_with


def first_task(strings: Iterable[str]) -> int:
    """ Решение первой задачи """

    def enough_vowels(string):
        vowels = frozenset('aeiou')
        return len([char for char in string if char in vowels]) >= 3

    def double_letter(string):
        return any(zip_with(lambda prev, curr: prev == curr, string, string[1::]))

    def no_forbidden_strings(string):
        naughty_strings = {('a', 'b'), ('c', 'd'), ('p', 'q'), ('x', 'y')}
        return not any(zip_with(lambda prev, curr: (prev, curr) in naughty_strings, string, string[1::]))

    rules = (enough_vowels, double_letter, no_forbidden_strings)
    return len([string for string in strings if all(rule(string) for rule in rules)])


def second_task(strings: Iterable[str]) -> int:
    """ Решение второй задачи """

    def two_letters_twice(string: str) -> bool:
        return re.search(r'([a-z][a-z]).*\1', string) is not None

    def same_letter_with_one_between(string: str) -> bool:
        def good_enough(left, _, right):
            return left == right

        return any(zip_with(good_enough, string, string[1::], string[2::]))

    rules = (two_letters_twice, same_letter_with_one_between)
    return len([string for string in strings if all(rule(string) for rule in rules)])
