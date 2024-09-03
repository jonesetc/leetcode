from json import dumps
from itertools import accumulate

import click

TEST_CASES = [
    [[5, 1, 5], 22],
    [[3, 4, 1, 2], 25],
]

EXPECTED = [
    0,
    1,
]


@click.command("1894")
def problem_1894():
    for case, expected in zip(TEST_CASES, EXPECTED, strict=True):
        actual = solution(3 * case)
        correct = dumps(actual) == dumps(expected)
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
