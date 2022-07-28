from utils.binary_tree import TreeNode, to_tree


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        # recursion version
        def check(root: TreeNode | None, lower: float | int, upper: float | int) -> bool:
            if not root:
                return True
            if not (lower < root.val < upper):
                return False
            return check(root.left, lower, root.val) and check(root.right, root.val, upper)
        return check(root, float("-inf"), float("inf"))

    def iterative_isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        stack: list[TreeNode] = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and root.val <= prev.val:
                return False
            prev = root
            root = root.right
        return True


def test_is_valid_bst():
    assert Solution().isValidBST(to_tree([0])) is True
    assert Solution().isValidBST(to_tree([2, 1, 3])) is True
    assert Solution().isValidBST(to_tree([5, 1, 4, None, None, 3, 6])) is False
    assert Solution().isValidBST(to_tree([5, 4, 6, None, None, 3, 7])) is False


def test_is_valid_bst_iterative():
    assert Solution().iterative_isValidBST(to_tree([0])) is True
    assert Solution().iterative_isValidBST(to_tree([2, 1, 3])) is True
    assert Solution().iterative_isValidBST(to_tree([5, 1, 4, None, None, 3, 6])) is False
    assert Solution().iterative_isValidBST(to_tree([5, 4, 6, None, None, 3, 7])) is False
