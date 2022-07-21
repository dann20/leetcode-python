from utils.linked_list import ListNode, to_linked_list, to_list


class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head:
            return None

        res = ListNode(-100, head)
        idx_left, idx_right = 1, 1
        ptr_before_left, tmp_prev = res, res
        ptr_left, ptr_right = head, head

        while idx_left <= left or idx_right <= right:
            if idx_left == left:
                ptr_left = head
                ptr_before_left = tmp_prev
            if idx_right == right:
                ptr_right = head
            idx_left += 1
            idx_right += 1
            tmp_prev = head
            head = head.next

        prev = ptr_right.next
        ptr_right.next = None
        sub_head = ptr_left
        while sub_head and sub_head.next:
            next_node = sub_head.next
            sub_head.next = prev
            prev = sub_head
            sub_head = next_node
        sub_head.next = prev
        ptr_before_left.next = sub_head

        return res.next


def test_reverse_between():
    assert to_list(Solution().reverseBetween(to_linked_list([1, 2, 3, 4, 5]), 2, 4)) == [1, 4, 3, 2, 5]
    assert to_list(Solution().reverseBetween(to_linked_list([1, 2, 3, 4, 5]), 1, 2)) == [2, 1, 3, 4, 5]
    assert to_list(Solution().reverseBetween(to_linked_list([1, 2, 3, 4, 5]), 1, 1)) == [1, 2, 3, 4, 5]
    assert to_list(Solution().reverseBetween(to_linked_list([1, 2, 3, 4, 5]), 1, 3)) == [3, 2, 1, 4, 5]
    assert to_list(Solution().reverseBetween(to_linked_list([1, 2, 3, 4, 5, 6]), 1, 4)) == [4, 3, 2, 1, 5, 6]
    assert to_list(Solution().reverseBetween(to_linked_list([1, 2, 3, 4, 5, 6]), 1, 6)) == [6, 5, 4, 3, 2, 1]
    assert to_list(Solution().reverseBetween(to_linked_list([1, 2, 3, 4, 5, 6]), 3, 5)) == [1, 2, 5, 4, 3, 6]
