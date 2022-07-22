from utils.linked_list import ListNode, to_list, to_linked_list


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def test_middle_node():
    assert to_list(Solution().middleNode(to_linked_list([1, 2, 3, 4, 5]))) == [3, 4, 5]
    assert to_list(Solution().middleNode(to_linked_list([1, 2, 3, 4, 5, 6]))) == [4, 5, 6]
