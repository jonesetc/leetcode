import click

from ..judge import json_judge
from ..test_cases import filter_and_zip


TEST_CASES = [
    [[1, 2, 3, 4], 2, 2],
    [[1, 2, 3], 1, 3],
    [[1, 2], 1, 1],
]

EXPECTED = [
    [[1, 2], [3, 4]],
    [[1, 2, 3]],
    [],
]


@click.command("2022")
@click.argument("test-cases", nargs=-1, type=click.IntRange(0, len(TEST_CASES) - 1))
def problem(test_cases: list[int]):
    for case, expected in filter_and_zip(TEST_CASES, EXPECTED, test_cases):
        print(f"{case=}", end=" ")
        actual = solution2(*case)
        correct = json_judge(actual, expected)
        print(f"{correct=} {expected=} {actual=}")


def solution(original: list[int], m: int, n: int) -> list[list[int]]:
    if m * n != len(original):
        return []
    else:
        return [original[i : i + n] for i in range(0, len(original), n)]


def solution2(original: list[int], m: int, n: int) -> list[list[int]]:
    if m * n != len(original):
        return []
    else:
        return list(zip(*([iter(original)] * n)))
