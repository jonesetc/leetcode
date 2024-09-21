from itertools import accumulate
from bisect import bisect_right

import click

from ..judge import simple_judge

TEST_CASES = [
    [[5, 1, 5], 22],
    [[3, 4, 1, 2], 25],
]

EXPECTED = [
    0,
    1,
]


@click.command("1894")
def problem():
    for case, expected in zip(TEST_CASES, EXPECTED, strict=True):
        actual = solution3(*case)
        correct = simple_judge(actual, expected)
        print(f"{case=} {correct=} {expected=} {actual=}")


def solution(chalk: list[int], k: int) -> int:
    remaining = k % sum(chalk)
    for i, curr in enumerate(chalk):
        remaining -= curr
        if remaining < 0:
            return i


def solution2(chalk: list[int], k: int) -> int:
    remaining = k % sum(chalk)
    for i, curr in enumerate(accumulate(chalk)):
        if curr > remaining:
            return i


def solution3(chalk: list[int], k: int) -> int:
    summed = list(accumulate(chalk))
    return bisect_right(summed, k % summed[-1])
