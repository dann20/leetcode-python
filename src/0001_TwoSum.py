class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_tbl = dict()
        for idx, val in enumerate(nums):
            if target - val in hash_tbl:
                return [hash_tbl[target - val], idx]
            else:
                hash_tbl[val] = idx
        return []


def test_twoSum():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]
