from json import dumps

import click

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
def problem_2022():
    for case, expected in zip(TEST_CASES, EXPECTED, strict=True):
        actual = solution2(*case)
        correct = dumps(actual) == dumps(expected)
        print(f"{case=} {correct=} {expected=} {actual=}")


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
