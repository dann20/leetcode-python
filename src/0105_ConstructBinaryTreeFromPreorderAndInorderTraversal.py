from utils.binary_tree import TreeNode, to_breadth_first_list as to_list


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        traversed = set()

        idx = 0
        while idx < len(inorder) and inorder[idx] != root.val:
            traversed.add(inorder[idx])
            idx += 1
        idx_inorder = idx

        idx = 1
        while idx < len(preorder) and preorder[idx] in traversed:
            idx += 1
        idx_preorder = idx

        root.left = self.buildTree(preorder[1:idx_preorder], inorder[:idx_inorder])
        root.right = self.buildTree(preorder[idx_preorder:], inorder[idx_inorder + 1:])

        return root


def test_build_tree():
    assert to_list(
        Solution().buildTree(
            [3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    ) == [3, 9, 20, 15, 7]
    assert to_list(Solution().buildTree([-1], [-1])) == [-1]
    assert to_list(
        Solution().buildTree(
            [1, 2, 4, 5, 8, 3, 6, 9, 10, 7, 11], [4, 2, 8, 5, 1, 9, 6, 10, 3, 7, 11]
        )
    ) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
