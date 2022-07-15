from utils.linked_list import ListNode, to_linked_list, to_list


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(-200, head)
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next

        return dummy.next


def test_delete_duplicates():
    s = Solution()
    assert to_list(s.deleteDuplicates(to_linked_list([1, 2, 3, 3, 4, 4, 5]))) == [1, 2, 5]
    assert to_list(s.deleteDuplicates(to_linked_list([1, 1, 1, 2, 3]))) == [2, 3]
