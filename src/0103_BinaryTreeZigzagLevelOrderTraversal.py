from utils.binary_tree import TreeNode, to_tree


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        res = [[root.val]]
        level = [root.left, root.right]
        while any(level):
            res.append([])
            new_level = []
            for node in level:
                if isinstance(node, TreeNode):
                    res[-1].append(node.val)
                    new_level.append(node.left)
                    new_level.append(node.right)
                else:
                    res[-1].append(node)
            level = new_level

        # remove None in each level
        res = [[val for val in level if val] for level in res]

        # remove empty level
        res = [level for level in res if level]

        # reverse levels alternatively
        res = [res[i] if i % 2 == 0 else list(reversed(res[i])) for i in range(len(res))]

        return res


def test_zigzag_level_order():
    assert Solution().zigzagLevelOrder(to_tree([3, 9, 20, None, None, 15, 7])) == [[3], [20, 9], [15, 7]]
    assert Solution().zigzagLevelOrder(to_tree([1])) == [[1]]
    assert Solution().zigzagLevelOrder(to_tree([])) == []
    tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))
    assert Solution().zigzagLevelOrder(tree) == [[1], [2], [3], [4], [5]]
