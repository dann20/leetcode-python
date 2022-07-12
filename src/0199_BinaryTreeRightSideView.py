from utils.binary_tree import TreeNode, to_tree


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        all_levels = [[root.val]]
        level = [root.left, root.right]
        while any(level):
            all_levels.append([])
            new_level = []
            for node in level:
                if isinstance(node, TreeNode):
                    all_levels[-1].append(node.val)
                    new_level.append(node.left)
                    new_level.append(node.right)
                else:
                    all_levels[-1].append(node)
            level = new_level

        # remove None in each level
        all_levels = [[val for val in level if val] for level in all_levels]

        # remove empty level
        all_levels = [level for level in all_levels if level]

        # get last node in each level
        res = [level[-1] for level in all_levels]

        return res


def test_right_side_view():
    assert Solution().rightSideView(to_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert Solution().rightSideView(to_tree([1, 2, 3, 7, 8, 4, 5, None, None, None, None, None, 6, None, None])) == [1, 3, 5, 6]
    assert Solution().rightSideView(to_tree([1, None, 3])) == [1, 3]
    assert Solution().rightSideView(to_tree([])) == []
