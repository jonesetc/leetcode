from json import dumps

import click

TEST_CASES = [
    [[1, 1, 2]],
    [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]],
]

EXPECTED = [
    2,
    5,
]


@click.command("26")
def problem_26():
    for case, expected in zip(TEST_CASES, EXPECTED, strict=True):
        actual = solution(*case)
        correct = dumps(actual) == dumps(expected)
        print(f"{case=} {correct=} {expected=} {actual=}")


def solution(nums: list[int]) -> int:
    last_seen = nums[0]
    last_dupe_index = 1

    for i, element in enumerate(nums[1:]):
        if element != last_seen:
            last_seen = element
            nums[last_dupe_index] = element
            last_dupe_index += 1

    return last_dupe_index
