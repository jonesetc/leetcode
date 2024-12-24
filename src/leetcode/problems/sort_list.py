from ..judge import simple_judge
from ..problem import AbstractProblem, ProblemCommand
from ..linked_list import ListNode, linked_list_to_list, list_to_linked_list


class Problem(AbstractProblem, metaclass=ProblemCommand, filename=__file__):
    TEST_CASES = [
        [[4, 2, 1, 3]],
        [[-1, 5, 3, 4, 0]],
        [[]],
    ]

    EXPECTED = [
        [1, 2, 3, 4],
        [-1, 0, 3, 4, 5],
        [],
    ]

    @staticmethod
    def solution(l: list[int]):
        return linked_list_to_list(Problem.real_solution(list_to_linked_list(l)))

    @staticmethod
    def real_solution(head: ListNode[int] | None) -> ListNode[int] | None:
        def split_at_pivot(start):
            ptr = start

            while start.next is not None and start.next.next is not None:
                ptr = ptr.next
                start = start.next.next

            if (mid := ptr.next) is not None:
                ptr.next = None
                return mid
            return None

        def merge(first, second):
            start = ListNode(0)
            ptr = start

            while first is not None and second is not None:
                if first.val < second.val:
                    ptr.next = first
                    first = first.next
                else:
                    ptr.next = second
                    second = second.next
                ptr = ptr.next

            if first is not None:
                ptr.next = first
            else:
                ptr.next = second

            return start.next

        def sort(start):
            if start is None or start.next is None:
                return start

            split = split_at_pivot(start)

            return merge(sort(start), sort(split))

        return sort(head)
