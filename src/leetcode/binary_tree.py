from dataclasses import dataclass
from typing import Self


@dataclass
class TreeNode[T]:
    val: T
    left: Self | None = None
    right: Self | None = None


def list_to_breadth_first_binary_tree[T](l: list[T | None]) -> TreeNode[T] | None:
    length = len(l)
    node_list = [TreeNode(element) if element is not None else None for element in l]

    for i, node in enumerate(node_list):
        if node is not None:
            node.left = node_list[(i * 2) + 1] if length > (i * 2) + 1 else None
            node.right = node_list[(i * 2) + 2] if length > (i * 2) + 2 else None

    return node_list[0] if length > 0 else None
