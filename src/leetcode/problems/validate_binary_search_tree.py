from ..binary_tree import TreeNode, list_to_breadth_first_binary_tree
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[2, 1, 3]],
        [[5, 1, 4, None, None, 3, 6]],
    ]

    EXPECTED = [
        True,
        False,
    ]

    @staticmethod
    def solution(root: list[int | None]) -> bool:
        return Problem.real_solution(list_to_breadth_first_binary_tree(root))

    @staticmethod
    def real_solution(root: TreeNode[int]) -> bool:
        def traverse(node):
            if node is None:
                return

            yield from traverse(node.left)
            yield node.val
            yield from traverse(node.right)

        prev = None

        for val in traverse(root):
            if prev is not None and prev >= val:
                return False
            prev = val

        return True
