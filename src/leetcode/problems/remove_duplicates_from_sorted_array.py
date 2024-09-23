from ..judge import beginning_list_judge
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[1, 1, 2]],
        [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]],
    ]

    EXPECTED = [
        [1, 2],
        [0, 1, 2, 3, 4],
    ]

    @staticmethod
    def judge(test_case_after_solution, solution, expected):
        return test_case_after_solution[0], beginning_list_judge(
            test_case_after_solution[0], expected, solution
        )

    @staticmethod
    def solution(nums: list[int]) -> int:
        last_seen = nums[0]
        last_dupe_index = 1

        for i, element in enumerate(nums[1:]):
            if element != last_seen:
                last_seen = element
                nums[last_dupe_index] = element
                last_dupe_index += 1

        return last_dupe_index
