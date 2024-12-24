from ..binary_tree import TreeNode
from ..judge import simple_judge
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[-10, -3, 0, 5, 9]],
        [[1, 3]],
    ]

    EXPECTED = [
        TreeNode(
            0,
            TreeNode(-3, TreeNode(-10, None, None), None),
            TreeNode(9, TreeNode(5, None, None), None),
        ),
        TreeNode(3, TreeNode(1, None, None), None),
    ]

    @staticmethod
    def judge(test_case_after_solution, solution, expected):
        return solution, simple_judge(solution, expected)

    @staticmethod
    def solution(nums: list[int]) -> TreeNode[int] | None:
        def build_bst_from_sorted_list(l):
            if len(l) == 0:
                return None

            pivot = len(l) // 2

            return TreeNode(
                l[pivot],
                build_bst_from_sorted_list(l[:pivot]),
                build_bst_from_sorted_list(l[pivot + 1 :]),
            )

        return build_bst_from_sorted_list(nums)
