from typing import no_type_check

from utils.linked_list import ListNode, to_linked_list, to_list


class Solution:
    @no_type_check
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        res = ListNode(0, head)
        left, right = res, head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return res.next


def test_remove_nth_from_end():
    assert to_list(
        Solution().removeNthFromEnd(to_linked_list([1, 2, 3, 4, 5]), 2)
    ) == to_list(to_linked_list([1, 2, 3, 5]))

    assert to_list(Solution().removeNthFromEnd(to_linked_list([1]), 1)) == to_list(
        to_linked_list([])
    )

    assert to_list(Solution().removeNthFromEnd(to_linked_list([1, 2]), 1)) == to_list(
        to_linked_list([1])
    )
