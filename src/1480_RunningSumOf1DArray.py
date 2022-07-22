class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = [0] * (len(nums) + 1)
        for idx, num in enumerate(nums):
            res[idx + 1] = res[idx] + num
        return res[1:]


def test_running_sum():
    assert Solution().runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert Solution().runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert Solution().runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
