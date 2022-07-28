from functools import lru_cache


class Solution:
    cache: dict[int, int] = {}

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        elif n in self.cache:
            return self.cache[n]
        else:
            self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
            return self.cache[n]

    @lru_cache(maxsize=30)
    def fib_2(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib_2(n - 1) + self.fib_2(n - 2)


def test_fib():
    assert Solution().fib(1) == 1
    assert Solution().fib(2) == 1
    assert Solution().fib(3) == 2
    assert Solution().fib(4) == 3
    assert Solution().fib(5) == 5
    assert Solution().fib(20) == 6765
    assert Solution().fib(28) == 317811
    assert Solution().fib(30) == 832040


def test_fib_2():
    assert Solution().fib_2(1) == 1
    assert Solution().fib_2(2) == 1
    assert Solution().fib_2(3) == 2
    assert Solution().fib_2(4) == 3
    assert Solution().fib_2(5) == 5
    assert Solution().fib_2(20) == 6765
    assert Solution().fib_2(28) == 317811
    assert Solution().fib_2(30) == 832040
