from ..judge import list_judge
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
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

    @staticmethod
    def judge(test_case_after_solution, solution, expected):
        return test_case_after_solution[0], list_judge(
            test_case_after_solution[0], expected
        )

    @staticmethod
    def solution(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        nums1.sort()

    @staticmethod
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
