class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1 for _ in range(len(nums))]

        prefix = 1
        for idx, num in enumerate(nums):
            ans[idx] *= prefix
            prefix *= num

        prefix = 1
        for idx, num in enumerate(reversed(nums)):
            ans[-idx - 1] *= prefix
            prefix *= num

        return ans


def test_product_except_self():
    s = Solution()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
