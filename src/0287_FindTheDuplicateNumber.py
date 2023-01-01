class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast, entry = nums[0], nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while slow != entry:
                    slow = nums[slow]
                    entry = nums[entry]
                return entry


def test_find_duplicate():
    assert Solution().findDuplicate([1, 3, 4, 2, 2]) == 2
    assert Solution().findDuplicate([3, 1, 3, 4, 2]) == 3
