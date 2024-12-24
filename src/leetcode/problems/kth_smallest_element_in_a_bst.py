from ..binary_tree import TreeNode, list_to_breadth_first_binary_tree
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[3, 1, 4, None, 2], 1],
        [[5, 3, 6, 2, 4, None, None, 1], 3],
    ]

    EXPECTED = [
        1,
        3,
    ]

    @staticmethod
    def solution(root: list[int | None], k: int) -> int:
        return Problem.real_solution(list_to_breadth_first_binary_tree(root), k)

    @staticmethod
    def real_solution(root: TreeNode[int], k: int) -> int:
        def traverse(node):
            if node is None:
                return

            yield from traverse(node.left)
            yield node.val
            yield from traverse(node.right)

        for i, val in enumerate(traverse(root)):
            if i + 1 == k:
                return val
