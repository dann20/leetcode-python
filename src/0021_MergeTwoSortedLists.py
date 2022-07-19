from utils.linked_list import ListNode, to_linked_list


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        match (bool(list1), bool(list2)):
            case (False, False): return None
            case (True, False): return list1
            case (False, True): return list2

        head = ListNode(0)
        res = head

        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        head.next = list2 if not list1 else list1

        return res.next


def test_merge_two_lists():
    assert Solution().mergeTwoLists(to_linked_list([1, 2, 4]), to_linked_list([1, 3, 4])) == to_linked_list([1, 1, 2, 3, 4, 4])
    assert Solution().mergeTwoLists(to_linked_list([1, 2, 4]), to_linked_list([])) == to_linked_list([1, 2, 4])
    assert Solution().mergeTwoLists(to_linked_list([]), to_linked_list([1, 3, 4])) == to_linked_list([1, 3, 4])
    assert Solution().mergeTwoLists(to_linked_list([]), to_linked_list([])) == to_linked_list([])
    assert Solution().mergeTwoLists(to_linked_list([1, 2, 4]), to_linked_list([1, 3, 4, 5])) == to_linked_list([1, 1, 2, 3, 4, 4, 5])
