from utils.binary_tree import TreeNode, to_tree


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        from copy import copy as c

        def dfs(root: TreeNode, res: list[list[int]], path: list[int] = []):
            path += [root.val]
            if not root.left and not root.right and sum(path) == targetSum:
                res.append(path)
            if root.left:
                dfs(root.left, res, c(path))
            if root.right:
                dfs(root.right, res, c(path))

        res: list[list[int]] = []
        if not root:
            return res

        dfs(root, res, [])
        return res


def test_path_sum():
    assert Solution().pathSum(
        to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22
    ) == [[5, 4, 11, 2], [5, 8, 4, 5]]
    assert Solution().pathSum(to_tree([1, 2, 3]), 5) == []
    assert Solution().pathSum(to_tree([1, 2]), 0) == []
    assert Solution().pathSum(to_tree([]), 0) == []
