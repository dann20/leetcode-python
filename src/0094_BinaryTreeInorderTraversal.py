from utils.binary_tree import TreeNode, to_tree


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        res = []
        stack: list[TreeNode] = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def inorder(self, root: TreeNode | None) -> list[int]:
        # recursive version
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


def test_inorder_traversal():
    assert Solution().inorderTraversal(to_tree([0])) == [0]
    assert Solution().inorderTraversal(to_tree([1])) == [1]
    assert Solution().inorderTraversal(to_tree([2, 1, 3])) == [1, 2, 3]
    assert Solution().inorderTraversal(to_tree([5, 1, 4, None, None, 3, 6])) == [1, 5, 3, 4, 6]
    assert Solution().inorderTraversal(to_tree([1, None, 2, 3, None])) == [1, 3, 2]


def test_inorder_recursion():
    assert Solution().inorder(to_tree([0])) == [0]
    assert Solution().inorder(to_tree([1])) == [1]
    assert Solution().inorder(to_tree([2, 1, 3])) == [1, 2, 3]
    assert Solution().inorder(to_tree([5, 1, 4, None, None, 3, 6])) == [1, 5, 3, 4, 6]
    assert Solution().inorder(to_tree([1, None, 2, 3, None])) == [1, 3, 2]
