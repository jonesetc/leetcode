from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode[T]:
    val: T
    next: Optional["ListNode[T]"] = None


def list_to_linked_list[T](
    l: list[T], loop_tail_to: int | None = None
) -> ListNode[T] | None:
    if len(l) == 0:
        return None

    head = None
    tail = None
    loop_to = None

    for i, element in enumerate(l):
        node = ListNode(element)

        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = tail.next

        if loop_tail_to == i:
            loop_to = node

    tail.next = loop_to

    return head
