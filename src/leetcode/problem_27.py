from json import dumps

import click

TEST_CASES = [
    [[3, 2, 2, 3], 3],
    [[0, 1, 2, 2, 3, 0, 4, 2], 2],
]

EXPECTED = [
    2,
    5,
]


@click.command("27")
def problem_27():
    for case, expected in zip(TEST_CASES, EXPECTED, strict=True):
        actual = solution2(*case)
        correct = dumps(actual) == dumps(expected)
        print(f"{case=} {correct=} {expected=} {actual=}")


def solution(nums: list[int], val: int) -> int:
    tally = len(nums)

    for i, element in enumerate(nums):
        if element == val:
            nums[i] = 999
            tally -= 1
    nums.sort()

    return tally


def solution2(nums: list[int], val: int) -> int:
    tally = 0

    for i, element in enumerate(nums):
        if element != val:
            nums[tally] = element
            tally += 1

    return tally
