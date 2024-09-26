from ..linked_list import ListNode, list_to_linked_list, linked_list_to_list
from ..problem import AbstractProblem, ProblemCommand


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[2, 4, 3], [5, 6, 4]],
        [[0], [0]],
        [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]],
    ]

    EXPECTED = [
        [7, 0, 8],
        [0],
        [8, 9, 9, 9, 0, 0, 0, 1],
    ]

    @staticmethod
    def solution(l1: list[int], l2: list[int]) -> list[int]:
        return linked_list_to_list(
            Problem.real_solution(
                list_to_linked_list(l1),
                list_to_linked_list(l2),
            )
        )

    @staticmethod
    def real_solution(
        l1: ListNode[int] | None, l2: ListNode[int] | None
    ) -> ListNode[int] | None:
        first_ptr = l1
        second_ptr = l2

        sum_head = ListNode(0)
        sum_ptr = sum_head

        carry = 0

        while first_ptr is not None or second_ptr is not None:
            curr_sum = (
                (first_ptr.val if first_ptr is not None else 0)
                + (second_ptr.val if second_ptr is not None else 0)
                + carry
            )
            sum_ptr.next = ListNode(curr_sum % 10)
            sum_ptr = sum_ptr.next
            carry = curr_sum // 10

            first_ptr = first_ptr.next if first_ptr is not None else None
            second_ptr = second_ptr.next if second_ptr is not None else None

        if carry != 0:
            sum_ptr.next = ListNode(carry)

        return sum_head.next
