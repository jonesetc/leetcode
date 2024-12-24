from ..binary_tree import TreeNode, list_to_breadth_first_binary_tree
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[4, 2, 6, 1, 3]],
        [[1, 0, 48, None, None, 12, 49]],
    ]

    EXPECTED = [
        1,
        1,
    ]

    @staticmethod
    def solution(root: list[int | None]) -> int:
        return Problem.real_solution(list_to_breadth_first_binary_tree(root))

    @staticmethod
    def real_solution(root: TreeNode[int]) -> int:
        def traverse(node):
            if node is None:
                return

            yield from traverse(node.left)
            yield node.val
            yield from traverse(node.right)

        prev = None
        min_diff = 10**10

        for val in traverse(root):
            if prev is not None:
                min_diff = min(min_diff, val - prev)
            prev = val

        return min_diff
