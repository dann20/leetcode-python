class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = -float("inf")
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if max_sum < cur_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum


def test_max_subarray():
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().maxSubArray([-2, 1]) == 1
    assert Solution().maxSubArray([1]) == 1
    assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23
