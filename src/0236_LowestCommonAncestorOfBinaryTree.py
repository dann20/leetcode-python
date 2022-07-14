from utils.binary_tree import TreeNode, to_tree


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        from copy import copy as c

        def pathfinder(root: TreeNode, node: TreeNode, path: list[TreeNode]) -> list[TreeNode]:
            if not root:
                return None
            elif root.val == node.val:
                path += [root]
                return path
            else:
                path += [root]
                left_path = pathfinder(root.left, node, c(path))
                right_path = pathfinder(root.right, node, c(path))

            if left_path:
                return left_path
            if right_path:
                return right_path

        path_p = pathfinder(root, p, [])
        path_q = pathfinder(root, q, [])

        common_path = [node_p for node_p, node_q in zip(path_p, path_q) if node_p == node_q]
        lca = common_path[-1]
        return lca


def test_LCA():
    tree = to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p, q = tree.left, tree.right
    assert Solution().lowestCommonAncestor(tree, p, q) == tree

    p, q = tree.left, tree.left.right.right
    assert Solution().lowestCommonAncestor(tree, p, q) == tree.left

    tree = to_tree([1, 2])
    p, q = tree, tree.left
    assert Solution().lowestCommonAncestor(tree, p, q) == tree
