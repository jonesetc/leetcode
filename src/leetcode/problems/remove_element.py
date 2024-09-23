from ..judge import beginning_list_judge
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[3, 2, 2, 3], 3],
        [[0, 1, 2, 2, 3, 0, 4, 2], 2],
    ]

    EXPECTED = [
        [2, 2],
        [0, 1, 4, 0, 3],
    ]

    @staticmethod
    def judge(test_case_after_solution, solution, expected):
        return test_case_after_solution[0], beginning_list_judge(
            test_case_after_solution[0], expected, solution, ordered=False
        )

    @staticmethod
    def solution(nums: list[int], val: int) -> int:
        tally = len(nums)

        for i, element in enumerate(nums):
            if element == val:
                nums[i] = 999
                tally -= 1
        nums.sort()

        return tally

    @staticmethod
    def solution2(nums: list[int], val: int) -> int:
        tally = 0

        for i, element in enumerate(nums):
            if element != val:
                nums[tally] = element
                tally += 1

        return tally
