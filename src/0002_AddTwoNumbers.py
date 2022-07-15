from utils.linked_list import ListNode, to_linked_list, to_list


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        cur = res
        c = 0

        while l1 or l2:
            tmp = l1.val + l2.val + c
            r, c = tmp % 10, tmp // 10
            cur.next = ListNode(r)
            cur, l1, l2 = cur.next, l1.next, l2.next
            if not l1 and l2:
                l1 = ListNode(0)
            if not l2 and l1:
                l2 = ListNode(0)

        if c:
            cur.next = ListNode(c)

        return res.next


def test_add_two_numbers():
    s = Solution()
    assert to_list(s.addTwoNumbers(to_linked_list([2, 4, 3]), to_linked_list([5, 6, 4]))) == [7, 0, 8]
    assert to_list(s.addTwoNumbers(to_linked_list([0]), to_linked_list([0]))) == [0]
    assert to_list(s.addTwoNumbers(to_linked_list([9, 9, 9, 9, 9, 9, 9]), to_linked_list([9, 9, 9, 9]))) == [8, 9, 9, 9, 0, 0, 0, 1]
