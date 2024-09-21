import click

from ..judge import beginning_list_judge

TEST_CASES = [
    [[1, 1, 2]],
    [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]],
]

EXPECTED = [
    [1, 2],
    [0, 1, 2, 3, 4],
]


@click.command("26")
def problem():
    for case, expected in zip(TEST_CASES, EXPECTED, strict=True):
        length = solution(*case)
        actual = case[0]
        correct = beginning_list_judge(case[0], expected, length)
        print(f"{case=} {correct=} {actual=} {expected=}")


def solution(nums: list[int]) -> int:
    last_seen = nums[0]
    last_dupe_index = 1

    for i, element in enumerate(nums[1:]):
        if element != last_seen:
            last_seen = element
            nums[last_dupe_index] = element
            last_dupe_index += 1

    return last_dupe_index