from utils.linked_list import ListNode


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        slow, fast, entry = head, head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                return entry
        return None

    def not_optimal(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        traversed = set()
        while head.next:
            if head in traversed:
                return head
            traversed.add(head)
            head = head.next

        return None


def test_detect_cycle():
    pass
