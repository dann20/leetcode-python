from utils.binary_tree import TreeNode, to_tree


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root

    def recursive_lca(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        elif p.val < root.val and q.val < root.val:
            return self.recursive_lca(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.recursive_lca(root.right, p, q)


def test_lca_bst():
    tree = to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p, q = tree.left, tree.right
    assert Solution().lowestCommonAncestor(tree, p, q).val == 6

    p, q = tree.left, tree.left.right
    assert Solution().lowestCommonAncestor(tree, p, q).val == 2

    tree = to_tree([2, 1, None])
    p, q = tree, tree.left
    assert Solution().lowestCommonAncestor(tree, p, q).val == 2


def test_lca_bst_recursion():
    tree = to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p, q = tree.left, tree.right
    assert Solution().recursive_lca(tree, p, q).val == 6

    p, q = tree.left, tree.left.right
    assert Solution().recursive_lca(tree, p, q).val == 2

    tree = to_tree([2, 1, None])
    p, q = tree, tree.left
    assert Solution().recursive_lca(tree, p, q).val == 2
