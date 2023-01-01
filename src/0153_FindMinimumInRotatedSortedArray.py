class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


def test_find_min():
    assert Solution().findMin([3, 4, 5, 1, 2]) == 1
    assert Solution().findMin([3, 4, 5, 6, 1, 2]) == 1
    assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert Solution().findMin([11, 13, 15, 17]) == 11
    assert Solution().findMin([5, 1, 2, 3, 4]) == 1
