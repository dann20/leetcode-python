class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        small, big = float("inf"), float("inf")
        for num in nums:
            if num <= small:
                small = num
            elif num <= big:
                big = num
            else:
                return True
        return False


def test_increasing_triplet():
    s = Solution()
    assert s.increasingTriplet([1, 2, 3, 4, 5]) is True
    assert s.increasingTriplet([5, 4, 3, 2, 1]) is False
    assert s.increasingTriplet([2, 1, 5, 4, 0, 6]) is True
    assert s.increasingTriplet([4, 3, 1, 8, 6, 7, 0, 9, 5, 2]) is True
