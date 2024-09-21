from ..judge import simple_judge

import click

TEST_CASES = [
    [1],
    [2],
    [3],
]

EXPECTED = [
    1,
    2,
    3,
]


@click.command("template")
def problem():
    for case, expected in zip(TEST_CASES, EXPECTED, strict=True):
        actual = solution(*case)
        correct = simple_judge(actual, expected)
        print(f"{case=} {correct=} {expected=} {actual=}")


def solution(expected: int) -> int:
    return expected
