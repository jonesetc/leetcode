from json import dumps

import click

TEST_CASES = [
    [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
    [[1], 1, [], 0],
    [[0], 0, [1], 1],
]

EXPECTED = [
    [1, 2, 2, 3, 5, 6],
    [1],
    [1],
]


@click.command("88")
def problem_88():
    for case, expected in zip(TEST_CASES, EXPECTED, strict=True):
        solution(*case)
        actual = case[0]
        correct = dumps(actual) == dumps(expected)
        print(f"{case=} {correct=} {expected=} {actual=}")


def solution(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums1[m:] = nums2[:n]
    nums1.sort()


def solution2(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    last_nums1 = m - 1
    last_nums2 = n - 1

    for i in reversed(range(0, m + n)):
        if last_nums2 < 0:
            break

        if last_nums1 >= 0 and nums1[last_nums1] > nums2[last_nums2]:
            nums1[i] = nums1[last_nums1]
            last_nums1 -= 1
        else:
            nums1[i] = nums2[last_nums2]
            last_nums2 -= 1
