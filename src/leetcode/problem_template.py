from json import dumps

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
def problem_template():
    for case, expected in zip(TEST_CASES, EXPECTED, strict=True):
        actual = solution(*case)
        correct = dumps(actual) == dumps(expected)
        print(f"{case=} {correct=} {expected=} {actual=}")


def solution(expected: int) -> int:
    return expected
