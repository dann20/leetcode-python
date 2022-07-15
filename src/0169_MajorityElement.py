class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        res = nums[0]
        for num in nums:
            count = count + 1 if num == res else count - 1
            if count < 0:
                res = num
                count = 1
        return res


def test_majority_element():
    assert Solution().majorityElement([3, 2, 3]) == 3
    assert Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
