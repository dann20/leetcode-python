class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        idx = 0
        left_sum, right_sum = 0, sum(nums[1:])
        while left_sum != right_sum and idx < len(nums):
            left_sum += nums[idx]
            right_sum -= nums[idx + 1] if idx < len(nums) - 1 else right_sum
            idx += 1
        return idx if idx < len(nums) else -1


def test_pivot_index():
    assert Solution().pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert Solution().pivotIndex([1, 2, 3]) == -1
    assert Solution().pivotIndex([-1, -1, -1, -1, -1, 0]) == 2
    assert Solution().pivotIndex([-1, -1, -1, 0, 1, 1]) == 0
    assert Solution().pivotIndex([2, 1, -1]) == 0
