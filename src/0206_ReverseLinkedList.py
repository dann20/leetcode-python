from utils.linked_list import ListNode, to_linked_list, to_list


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        prev = None
        cur: ListNode | None = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev

    def recursive_reverse(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        new_head = self.recursive_reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head


def test_reverse_list():
    assert to_list(Solution().reverseList(to_linked_list([1, 2, 3, 4, 5]))) == [
        5,
        4,
        3,
        2,
        1,
    ]
    assert to_list(Solution().reverseList(to_linked_list([1, 2, 3, 4, 5, 6]))) == [
        6,
        5,
        4,
        3,
        2,
        1,
    ]
    assert to_list(Solution().reverseList(to_linked_list([]))) == []
    assert to_list(Solution().reverseList(to_linked_list([1]))) == [1]


def test_recursive_reverse():
    assert to_list(Solution().recursive_reverse(to_linked_list([1, 2, 3, 4, 5]))) == [
        5,
        4,
        3,
        2,
        1,
    ]
    assert to_list(
        Solution().recursive_reverse(to_linked_list([1, 2, 3, 4, 5, 6]))
    ) == [6, 5, 4, 3, 2, 1]
    assert to_list(Solution().recursive_reverse(to_linked_list([]))) == []
    assert to_list(Solution().recursive_reverse(to_linked_list([1]))) == [1]
