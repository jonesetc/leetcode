import click


from ..judge import beginning_list_judge

TEST_CASES = [
    [[3, 2, 2, 3], 3],
    [[0, 1, 2, 2, 3, 0, 4, 2], 2],
]

EXPECTED = [
    [2, 2],
    [0, 1, 4, 0, 3],
]


@click.command("27")
def problem():
    for case, expected in zip(TEST_CASES, EXPECTED, strict=True):
        length = solution(*case)
        actual = case[0]
        correct = beginning_list_judge(case[0], expected, length, ordered=False)
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