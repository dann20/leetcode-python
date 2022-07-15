from utils.linked_list import ListNode, to_linked_list, to_list


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        dummy = ListNode(-1, head)
        prev = dummy

        while head and head.next:
            tmp = head.next
            prev.next = tmp
            head.next = tmp.next
            tmp.next = head
            prev = head
            head = head.next

        return dummy.next


def test_swap_pairs():
    s = Solution()
    assert to_list(s.swapPairs(to_linked_list([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert to_list(s.swapPairs(to_linked_list([]))) == []
    assert to_list(s.swapPairs(to_linked_list([1]))) == [1]
