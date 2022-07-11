class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            l, r = idx + 1, len(nums) - 1
            while l < r:
                tmp = val + nums[l] + nums[r]
                if tmp > 0:
                    r -= 1
                elif tmp < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


def test_3Sum():
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [
        [-1, -1, 2],
        [-1, 0, 1],
    ]
    assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert Solution().threeSum([]) == []
    assert Solution().threeSum([0]) == []
