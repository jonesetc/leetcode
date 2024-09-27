from collections import deque

from ..binary_tree import TreeNode, list_to_breadth_first_binary_tree
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [[[3, 9, 20, None, None, 15, 7]], [[1]], [[]]]

    EXPECTED = [[[3], [9, 20], [15, 7]], [[1]], []]

    @staticmethod
    def solution(root: list[int | None]) -> list[list[int]]:
        return Problem.real_solution(list_to_breadth_first_binary_tree(root))

    @staticmethod
    def real_solution(root: TreeNode[int] | None) -> list[list[int]]:
        if root is None:
            return []

        queue = deque([(root, 0)])
        vals = []

        while len(queue) > 0:
            node, index = queue.popleft()

            if len(vals) == index:
                vals.append([node.val])
            else:
                vals[index].append(node.val)

            if node.left is not None:
                queue.append((node.left, index + 1))
            if node.right is not None:
                queue.append((node.right, index + 1))

        return vals
