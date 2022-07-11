from utils.binary_tree import TreeNode, to_breadth_first_list as to_list


class Solution:
    def sortedArrayToBST(self, num: list[int]) -> TreeNode | None:
        if not num:
            return None
        mid = len(num) // 2
        cur = TreeNode(num[mid])
        cur.left = self.sortedArrayToBST(num[:mid])
        cur.right = self.sortedArrayToBST(num[mid + 1:])
        return cur


def test_sorted_array_to_bst():
    assert to_list(Solution().sortedArrayToBST([-10, -3, 0, 5, 9])) == [0, -3, 9, -10, 5]
    assert to_list(Solution().sortedArrayToBST([1, 3])) == [3, 1]
    assert to_list(Solution().sortedArrayToBST([0])) == [0]
