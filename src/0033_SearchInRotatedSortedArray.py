class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] <= nums[mid]:  # left partition is sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:  # right partition is sorted
                if target <= nums[mid] or target > nums[right]:
                    right = mid
                else:
                    left = mid + 1
        return left if nums[left] == target else -1


def test_search():
    assert Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
    assert Solution().search(nums=[2, 4, 5, 6, 7, 0, 1], target=0) == 5
    assert Solution().search(nums=[6, 7, 0, 1, 2, 4, 5], target=0) == 2
    assert Solution().search(nums=[5, 6, 7, 0, 1, 2, 4], target=0) == 3
    assert Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
    assert Solution().search(nums=[5, 1, 3], target=3) == 2
    assert Solution().search(nums=[3, 1], target=1) == 1
    assert Solution().search(nums=[1], target=0) == -1
