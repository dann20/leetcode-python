class Solution:
    def __init__(self, first_bad: int, n):
        self.check = [False for _ in range(first_bad - 1)] + [True for _ in range(first_bad - 1, n)]

    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def isBadVersion(self, k: int) -> bool:
        return self.check[k - 1]


def test_first_bad_version():
    s1 = Solution(6, 20)
    assert s1.firstBadVersion(20) == 6

    s2 = Solution(100, 123)
    assert s2.firstBadVersion(123) == 100

    s3 = Solution(259, 1293)
    assert s3.firstBadVersion(1293) == 259
