from functools import lru_cache


class Solution:
    @lru_cache(maxsize=45)
    def climbStairs(self, n: int) -> int:
        if 1 <= n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


def test_climbing_stairs():
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5
    assert Solution().climbStairs(5) == 8
    assert Solution().climbStairs(6) == 13
    assert Solution().climbStairs(7) == 21
