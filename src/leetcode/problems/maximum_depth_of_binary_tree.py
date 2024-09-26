from ..binary_tree import TreeNode, list_to_breadth_first_binary_tree
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[3, 9, 20, None, None, 15, 7]],
        [[1, None, 2]],
    ]

    EXPECTED = [
        3,
        2,
    ]

    @staticmethod
    def solution(root: list[int]) -> int:
        return Problem.real_solution(list_to_breadth_first_binary_tree(root))

    @staticmethod
    def real_solution(root: TreeNode[int] | None) -> int:
        nodes = [(1, root)] if root is not None else []
        max_depth = 0

        while len(nodes) > 0:
            depth, node = nodes.pop()
            if node is not None:
                nodes.append((depth + 1, node.left))
                nodes.append((depth + 1, node.right))
                max_depth = max(max_depth, depth)

        return max_depth

    @staticmethod
    def real_solution2(root: TreeNode[int] | None) -> int:
        if root is None:
            return 0
        else:
            return max(map(Problem.real_solution2, [root.left, root.right])) + 1
