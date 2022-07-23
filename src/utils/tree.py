from __future__ import annotations


class Node:
    def __init__(self, val: int | None = None, children: list[Node] | None = None) -> None:
        self.val = val
        self.children = children
