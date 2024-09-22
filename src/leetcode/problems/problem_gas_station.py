import click

from ..judge import simple_judge
from ..test_cases import filter_and_zip


TEST_CASES = [
    [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]],
    [[2, 3, 4], [3, 4, 3]],
]

EXPECTED = [
    3,
    -1,
]


@click.command("gas-station")
@click.argument("test-cases", nargs=-1, type=click.IntRange(0, len(TEST_CASES) - 1))
def problem(test_cases: list[int]):
    for case, expected in filter_and_zip(TEST_CASES, EXPECTED, test_cases):
        actual = solution(*case)
        correct = simple_judge(actual, expected)
        print(f"{case=} {correct=} {expected=} {actual=}")


def solution(gas: list[int], cost: list[int]) -> int:
    segments = {}
    segment_start = 0
    segment_required = 0

    for i, (g, c) in enumerate(zip(gas, cost)):
        if segment_required < 0:
            segments[segment_start] = segment_required
            segment_start = i
            segment_required = 0

        segment_required += g - c
    else:
        segments[segment_start] = segment_required

    if sum(segments.values()) < 0:
        return -1

    return sorted(segments, key=segments.get, reverse=True)[0]
