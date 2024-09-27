from collections import deque

from ..binary_tree import TreeNode, list_to_breadth_first_binary_tree
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[3, 9, 20, None, None, 15, 7]],
        [[3, 9, 20, 15, 7]],
    ]

    EXPECTED = [
        [3.0, 14.5, 11.0],
        [3.0, 14.5, 11.0],
    ]

    @staticmethod
    def solution(root: list[int | None]) -> list[float]:
        return Problem.real_solution(list_to_breadth_first_binary_tree(root))

    @staticmethod
    def real_solution(root: TreeNode[int]) -> list[float]:
        queue = deque([(root, 0)])
        sums = []

        while len(queue) > 0:
            node, index = queue.popleft()

            if len(sums) == index:
                sums.append((node.val, 1))
            else:
                sums[index] = (sums[index][0] + node.val, sums[index][1] + 1)

            if node.left is not None:
                queue.append((node.left, index + 1))
            if node.right is not None:
                queue.append((node.right, index + 1))

        return [total / count for total, count in sums]
