from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"(Val: {self.val}\tLeft: {self.left}\tRight: {self.right})"

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right

    def __ne__(self, other) -> bool:
        if other is None:
            return True
        return self.val != other.val or self.left != other.left or self.right != other.right


def to_tree(nums: list[int]) -> TreeNode | None:
    """
    Convert a breadth-first traversal list (including NULL) to a binary tree.
    Inverse operation of to_breadth_first_list function.

    Input: nums = [1, 2, 3, 4, 5, 6, 7]

    Output resembles root:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    """
    if not nums:
        return None
    elif len(nums) == 2:
        return TreeNode(nums[0], TreeNode(nums[1]))

    root = TreeNode(nums[0])
    queue = [root]
    i = 1
    while queue and i < len(nums):
        node = queue.pop(0)
        if nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1
        if nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1
    return root


def to_breadth_first_list(root: TreeNode | None) -> list[int]:
    """
    Convert a binary tree to a breadth-first traversal list (not including NULL).
    (Leetcode style without NULL)
    Inverse operation of to_tree function.

    Input:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    Output: [1, 2, 3, 4, 5, 6, 7]
    """
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res


def to_preorder_list(root: TreeNode | None) -> list[int]:
    """
    Convert a binary tree to a preorder list (not including NULL).
    (child to parent, left to right)

    Input:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    Output: [1, 2, 4, 5, 3, 6, 7]
    """
    if not root:
        return []
    return [root.val] + to_preorder_list(root.left) + to_preorder_list(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(to_breadth_first_list(root))
    print(to_preorder_list(root))

    print(to_breadth_first_list(to_tree([1, 2, 3, 4, 5, 6, 7])))
    print(to_breadth_first_list(to_tree([1, 2, 3, 4, None, 6, None])))
    print(root == to_tree([1, 2, 3, 4, 5, 6, 7]))
    print(root != to_tree([1, 2, 3, 4, 9, 6, 8]))
