from os import readv

from ..problem import AbstractProblem, ProblemCommand
from ..data_structures import ListNode, list_to_linked_list


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[3, 2, 0, -4], 1],
        [[1, 2], 0],
        [[1], -1],
    ]

    EXPECTED = [
        True,
        True,
        False,
    ]

    @staticmethod
    def solution(l: list[int], pos: int):
        return Problem.real_solution(list_to_linked_list(l, pos))

    @staticmethod
    def real_solution(head: ListNode | None) -> bool:
        trailing = head
        leading = head.next if head is not None else head

        while leading is not None:
            if leading == trailing:
                return True

            if (leading := leading.next) is not None:
                if leading == trailing:
                    return True
            else:
                return False

            leading = leading.next
            trailing = trailing.next

        return False