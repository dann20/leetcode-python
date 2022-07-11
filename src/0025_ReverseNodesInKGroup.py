from utils.linked_list import ListNode, to_linked_list, to_list


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        def check_enough_k(head: ListNode | None, k: int):
            if head is None:
                return False
            count = 0
            while head is not None:
                count += 1
                head = head.next
                if count == k:
                    return True
            return False

        def reverse(head: ListNode | None, k: int, prev_group: ListNode):
            if head is None:
                return

            prev = None
            new_prev_group = head
            if check_enough_k(head, k):
                for _ in range(k):
                    new_head = head.next
                    head.next = prev
                    prev = head
                    head = new_head
                prev_group.next = prev
                reverse(head, k, new_prev_group)
            else:
                prev_group.next = head
                return

        dummy = ListNode(-1, head)
        reverse(head, k, dummy)
        return dummy.next


def test_reverse_k_group():
    assert to_list(Solution().reverseKGroup(to_linked_list([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert to_list(Solution().reverseKGroup(to_linked_list([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
    assert to_list(Solution().reverseKGroup(to_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), 2)) == [2, 1, 4, 3, 6, 5, 8, 7]
    assert to_list(Solution().reverseKGroup(to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)) == [3, 2, 1, 6, 5, 4, 9, 8, 7, 10]
