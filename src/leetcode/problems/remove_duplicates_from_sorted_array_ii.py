import click

from ..command import get_problem_name
from ..judge import beginning_list_judge
from ..test_cases import filter_and_zip


TEST_CASES = [
    [[1, 1, 1, 2, 2, 3]],
    [[0, 0, 1, 1, 1, 1, 2, 3, 3]],
]

EXPECTED = [
    [1, 1, 2, 2, 3],
    [0, 0, 1, 1, 2, 3, 3],
]


@click.command(get_problem_name(__file__))
@click.argument("test-cases", nargs=-1, type=click.IntRange(0, len(TEST_CASES) - 1))
def problem(test_cases: list[int]):
    for case, expected in filter_and_zip(TEST_CASES, EXPECTED, test_cases):
        print(f"{case=}", end=" ")
        length = solution(*case)
        actual = case[0]
        correct = beginning_list_judge(case[0], expected, length)
        print(f"{correct=} {expected=} {actual=} {length=}")


def solution(nums: list[int]) -> int:
    if len(nums) < 3:
        return len(nums)

    last_dupe_index = 2

    for element in nums[2:]:
        if element != nums[last_dupe_index - 2]:
            nums[last_dupe_index] = element
            last_dupe_index += 1

    return last_dupe_index
