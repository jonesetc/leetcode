from ..judge import simple_judge
from ..problem import AbstractProblem, ProblemCommand
from ..linked_list import ListNode, linked_list_to_list, list_to_linked_list


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[1, 2, 4], [1, 3, 4]],
        [[], []],
        [[], [0]],
    ]

    EXPECTED = [
        [1, 1, 2, 3, 4, 4],
        [],
        [0],
    ]

    @staticmethod
    def solution(list1: list[int], list2: list[int]):
        return linked_list_to_list(
            Problem.real_solution(
                list_to_linked_list(list1), list_to_linked_list(list2)
            )
        )

    @staticmethod
    def real_solution(
        list1: ListNode[int] | None, list2: ListNode[int] | None
    ) -> ListNode[int] | None:
        head = ListNode(0)
        tail = head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return head.next
