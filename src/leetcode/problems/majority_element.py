from collections import Counter

from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
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

    @staticmethod
    def solution(nums: list[int]) -> int:
        return Counter(nums).most_common(1)[0][0]

    @staticmethod
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

    @staticmethod
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
