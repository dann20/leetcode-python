from utils.binary_tree import TreeNode, to_tree


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        def inorder(root: TreeNode | None) -> list[int]:
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        inorder_list = inorder(root)
        return inorder_list[k - 1]


def test_kth_smallest():
    assert Solution().kthSmallest(to_tree([3, 1, 4, None, 2]), 1) == 1
    assert Solution().kthSmallest(to_tree([5, 3, 6, 2, 4, None, None, 1, None]), 3) == 3
