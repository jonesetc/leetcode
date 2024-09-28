from collections import deque

from ..binary_tree import (
    TreeNode,
    list_to_breadth_first_binary_tree,
    breadth_first_binary_tree_to_list,
)
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[4, 2, 7, 1, 3, 6, 9]],
        [[2, 1, 3]],
        [[]],
    ]

    EXPECTED = [
        [4, 7, 2, 9, 6, 3, 1],
        [2, 3, 1],
        [],
    ]

    @staticmethod
    def solution(root: list[int | None]) -> list[int]:
        return breadth_first_binary_tree_to_list(
            Problem.real_solution(list_to_breadth_first_binary_tree(root))
        )

    @staticmethod
    def real_solution(root: TreeNode[int] | None) -> TreeNode[int] | None:
        if root is None:
            return root

        queue = deque([root])

        while len(queue) > 0:
            node = queue.popleft()

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

            node.left, node.right = node.right, node.left

        return root
