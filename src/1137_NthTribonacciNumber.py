class Solution:
    cache: dict[int, int] = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n not in self.cache:
            self.cache[n] = (
                self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            )
        return self.cache[n]


def test_tribonacci():
    assert Solution().tribonacci(3) == 2
    assert Solution().tribonacci(4) == 4
    assert Solution().tribonacci(25) == 1389537
