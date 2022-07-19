class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.val == other.val and self.next == other.next


def to_linked_list(nums: list) -> ListNode | None:
    if not nums:
        return None
    head = ListNode(nums[0])
    cur = head
    for num in nums[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head


def to_list(head: ListNode | None) -> list:
    if head is None:
        return []
    res = []
    while head is not None:
        res.append(head.val)
        head = head.next
    return res
