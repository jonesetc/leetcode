from collections import deque

from ..binary_tree import TreeNode, list_to_breadth_first_binary_tree
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[1, 2, 3, None, 5, None, 4]],
        [[1, None, 3]],
        [[]],
    ]

    EXPECTED = [
        [1, 3, 4],
        [1, 3],
        [],
    ]

    @staticmethod
    def solution(root: list[int | None]) -> list[int]:
        return Problem.real_solution(list_to_breadth_first_binary_tree(root))

    @staticmethod
    def real_solution(root: TreeNode[int] | None) -> list[int]:
        if root is None:
            return []

        queue = deque([(root, 0)])
        rightmost = []

        while len(queue) > 0:
            node, depth = queue.popleft()

            if len(rightmost) == depth:
                rightmost.append(node.val)

            if node.right is not None:
                queue.append((node.right, depth + 1))
            if node.left is not None:
                queue.append((node.left, depth + 1))

        return rightmost
