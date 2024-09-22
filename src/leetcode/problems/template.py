import click

from ..command import get_problem_name
from ..judge import simple_judge
from ..test_cases import filter_and_zip


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


@click.command(get_problem_name(__file__))
@click.argument("test-cases", nargs=-1, type=click.IntRange(0, len(TEST_CASES) - 1))
def problem(test_cases: list[int]):
    for case, expected in filter_and_zip(TEST_CASES, EXPECTED, test_cases):
        actual = solution(*case)
        correct = simple_judge(actual, expected)
        print(f"{case=} {correct=} {expected=} {actual=}")


def solution(expected: int) -> int:
    return expected
