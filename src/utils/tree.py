from __future__ import annotations


class Node:
    def __init__(self, val: int = 0, children: list[Node] | None = None) -> None:
        self.val = val
        self.children = children

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.val == other.val and self.children == other.children


if __name__ == '__main__':
    tree = Node(1, [Node(2, [Node(3), Node(4)]), Node(5, [Node(6), Node(7)])])
    tree2 = Node(1, [Node(2, [Node(3), Node(4)]), Node(5, [Node(6), Node(7)])])
    tree3 = Node(1, [Node(2, [Node(3), Node(4)]), Node(5, [Node(60), Node(7)])])

    assert tree == tree2
    assert tree != tree3

    print(tree)
    print(tree2)
    print(tree3)
