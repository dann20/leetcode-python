from utils.linked_list import ListNode, to_linked_list, to_list


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # prev == last_node, slow == None

        start = head
        end = prev
        while start.next and end.next:
            next_start = start.next
            next_end = end.next
            start.next = end
            end.next = next_start
            start = next_start
            end = next_end
        if end.next:
            start.next = end


def test_reorderList():
    inp1 = to_linked_list([1, 2, 3, 4, 5, 6])
    Solution().reorderList(inp1)
    assert to_list(inp1) == [1, 6, 2, 5, 3, 4]

    inp2 = to_linked_list([1, 2, 3, 4, 5])
    Solution().reorderList(inp2)
    assert to_list(inp2) == [1, 5, 2, 4, 3]
