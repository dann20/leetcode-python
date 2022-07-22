from utils.linked_list import ListNode, to_linked_list, to_list


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        if not head:
            return None

        left, right = ListNode(), ListNode()
        left_head, right_head = left, right

        while head:
            tmp = head.next
            head.next = None
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = tmp

        left.next = right_head.next
        return left_head.next


def test_partition():
    assert to_list(Solution().partition(to_linked_list([1, 4, 3, 2, 5, 2]), 3)) == [1, 2, 2, 4, 3, 5]
    assert to_list(Solution().partition(to_linked_list([2, 1]), 2)) == [1, 2]
    assert to_list(Solution().partition(to_linked_list([1]), 1)) == [1]
