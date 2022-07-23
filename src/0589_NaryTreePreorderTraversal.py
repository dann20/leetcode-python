from utils.tree import Node


class Solution:
    def preorder(self, root: Node) -> list[int]:
        # iterative version of preorder traversal of a n-ary tree
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            node = queue.pop()
            res.append(node.val)
            queue.extend(list(reversed(node.children)) if node.children else [])
        return res

    def preorder_recursion(self, root: Node) -> list[int]:
        if not root:
            return []

        res = [root.val]
        if not root.children:
            return res

        for child in root.children:
            res += self.preorder_recursion(child)
        return res


def test_preorder():
    assert Solution().preorder(None) == []
    assert Solution().preorder(Node(1)) == [1]
    assert Solution().preorder(Node(1, [Node(2), Node(3)])) == [1, 2, 3]
    assert Solution().preorder(Node(1, [Node(2, [Node(4), Node(5)])])) == [1, 2, 4, 5]
    assert Solution().preorder(Node(1, [Node(2, [Node(4), Node(5)]), Node(3)])) == [1, 2, 4, 5, 3]
    assert Solution().preorder(Node(1, [Node(2, [Node(4), Node(5)]), Node(3, [Node(6)])])) == [1, 2, 4, 5, 3, 6]
    assert Solution().preorder(Node(1, [Node(2, [Node(4), Node(5)]), Node(3, [Node(6), Node(7)])])) == [1, 2, 4, 5, 3, 6, 7]
    assert Solution().preorder(Node(1, [Node(2, [Node(4), Node(5), Node(8)]), Node(3, [Node(6), Node(7)]), Node(9)])) == [1, 2, 4, 5, 8, 3, 6, 7, 9]


def test_preorder_recursion():
    assert Solution().preorder_recursion(None) == []
    assert Solution().preorder_recursion(Node(1)) == [1]
    assert Solution().preorder_recursion(Node(1, [Node(2), Node(3)])) == [1, 2, 3]
    assert Solution().preorder_recursion(Node(1, [Node(2, [Node(4), Node(5)])])) == [1, 2, 4, 5]
    assert Solution().preorder_recursion(Node(1, [Node(2, [Node(4), Node(5)]), Node(3)])) == [1, 2, 4, 5, 3]
    assert Solution().preorder_recursion(Node(1, [Node(2, [Node(4), Node(5)]), Node(3, [Node(6)])])) == [1, 2, 4, 5, 3, 6]
    assert Solution().preorder_recursion(Node(1, [Node(2, [Node(4), Node(5)]), Node(3, [Node(6), Node(7)])])) == [1, 2, 4, 5, 3, 6, 7]
    assert Solution().preorder_recursion(Node(1, [Node(2, [Node(4), Node(5), Node(8)]), Node(3, [Node(6), Node(7)]), Node(9)])) == [1, 2, 4, 5, 8, 3, 6, 7, 9]
