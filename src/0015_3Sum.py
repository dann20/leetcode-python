class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ...


def test_3Sum():
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [
        [-1, -1, 2],
        [-1, 0, 1],
    ]
    assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert Solution().threeSum([]) == []
    assert Solution().threeSum([0]) == []
