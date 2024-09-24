import sys

from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [7, [2, 3, 1, 2, 4, 3]],
        [4, [1, 4, 4]],
        [11, [1, 1, 1, 1, 1, 1, 1, 1]],
    ]

    EXPECTED = [
        2,
        1,
        0,
    ]

    @staticmethod
    def solution1(target: int, nums: list[int]) -> int:
        min_length = sys.maxsize
        window_start = 0
        window_sum = 0

        for i, element in enumerate(nums):
            window_length = i - window_start + 1
            window_sum += element

            if window_sum < target:
                continue

            for leading_element in nums[window_start:i]:
                trimmed_window_sum = window_sum - leading_element
                if trimmed_window_sum < target:
                    break
                window_start += 1
                window_length -= 1
                window_sum = trimmed_window_sum

            if window_length < min_length:
                min_length = window_length

        return min_length if min_length != sys.maxsize else 0

    @staticmethod
    def solution(target: int, nums: list[int]) -> int:
        min_length = sys.maxsize
        window_start = 0
        window_sum = 0

        for i, element in enumerate(nums):
            window_sum += element

            while window_sum >= target:
                min_length = min(i - window_start + 1, min_length)
                window_sum -= nums[window_start]
                window_start += 1

        return min_length if min_length != sys.maxsize else 0
