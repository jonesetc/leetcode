from ..judge import beginning_list_judge
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[1, 1, 1, 2, 2, 3]],
        [[0, 0, 1, 1, 1, 1, 2, 3, 3]],
    ]

    EXPECTED = [
        [1, 1, 2, 2, 3],
        [0, 0, 1, 1, 2, 3, 3],
    ]

    @staticmethod
    def judge(test_case_after_solution, solution, expected):
        return test_case_after_solution[0], beginning_list_judge(
            test_case_after_solution[0], expected, solution
        )

    @staticmethod
    def solution(nums: list[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        last_dupe_index = 2

        for element in nums[2:]:
            if element != nums[last_dupe_index - 2]:
                nums[last_dupe_index] = element
                last_dupe_index += 1

        return last_dupe_index
