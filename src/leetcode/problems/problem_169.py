from collections import Counter

import click

from ..judge import simple_judge
from ..test_cases import filter_and_zip


TEST_CASES = [
    [[3, 2, 3]],
    [[2, 2, 1, 1, 1, 2, 2]],
    [[3, 3, 4]],
]

EXPECTED = [
    3,
    2,
    3,
]


@click.command("169")
@click.argument("test-cases", nargs=-1, type=click.IntRange(0, len(TEST_CASES) - 1))
def problem(test_cases: list[int]):
    for case, expected in filter_and_zip(TEST_CASES, EXPECTED, test_cases):
        print(f"{case=}", end=" ")
        actual = solution3(*case)
        correct = simple_judge(actual, expected)
        print(f"{correct=} {expected=} {actual=}")


def solution(nums: list[int]) -> int:
    return Counter(nums).most_common(1)[0][0]


def solution2(nums: list[int]) -> int:
    nums.sort()

    most_common = nums[0]
    longest_run = 1
    run_start = 0

    for i, element in enumerate(nums[1:]):
        if element != nums[run_start]:
            if longest_run < i - run_start + 1:
                most_common = element
                longest_run = i - run_start + 1
            run_start = i + 1
        elif longest_run < i - run_start + 2:
            most_common = element
            longest_run = i - run_start + 2

    return most_common


def solution3(nums: list[int]) -> int:
    most_common = nums[0]
    votes = 1

    for element in nums[1:]:
        if votes == 0:
            most_common = element

        if most_common != element:
            votes -= 1
        else:
            votes += 1

    return most_common
