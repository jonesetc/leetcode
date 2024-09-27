from ..binary_tree import TreeNode, list_to_breadth_first_binary_tree
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[1, 2, 3], [1, 2, 3]],
        [[1, 2], [1, None, 2]],
        [[1, 2, 1], [1, 1, 2]],
    ]

    EXPECTED = [
        True,
        False,
        False,
    ]

    @staticmethod
    def solution(p: list[int | None], q: list[int | None]) -> bool:
        return Problem.real_solution(
            list_to_breadth_first_binary_tree(p),
            list_to_breadth_first_binary_tree(q),
        )

    @staticmethod
    def real_solution(p: TreeNode[int] | None, q: TreeNode[int] | None) -> bool:
        nodes = [(p, q)]

        while len(nodes) > 0:
            node_p, node_q = nodes.pop()

            if (node_p is not None) and (node_q is not None):
                if node_p.val != node_q.val:
                    return False
                nodes.append((node_p.left, node_q.left))
                nodes.append((node_p.right, node_q.right))
            elif (node_p is not None) != (node_q is not None):
                return False

        return True
