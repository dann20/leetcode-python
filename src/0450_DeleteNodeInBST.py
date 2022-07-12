from utils.binary_tree import TreeNode, to_tree, to_breadth_first_list as to_list


class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        def delete_smallest(root: TreeNode):
            cur = root.left
            prev = root

            while cur.left:
                prev = cur
                cur = cur.left

            prev.left = cur.right
            return cur

        if not root:
            return root

        # Find key node
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root

        # Case: No child or only 1 child
        if not root.left and not root.right:
            return None
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Case: Two children
        if not root.right.left:
            root.right.left = root.left
            return root.right
        else:
            smallest = delete_smallest(root.right)
            smallest.left = root.left
            smallest.right = root.right
            return smallest


def test_delete_node():
    assert to_list(Solution().deleteNode(to_tree([5, 3, 6, 2, 4, None, 7]), 3)) == [5, 4, 6, 2, 7]
    assert to_list(Solution().deleteNode(to_tree([5, 3, 6, 2, 4, None, 7]), 0)) == [5, 3, 6, 2, 4, 7]
    assert to_list(Solution().deleteNode(to_tree([]), 0)) == []
