class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    def another_version(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= n - 1
        return count

    def using_builtin(self, n: int) -> int:
        return bin(n).count("1")


def test_hamming_weight():
    assert Solution().hammingWeight(11) == 3
    assert Solution().hammingWeight(128) == 1
    assert Solution().hammingWeight(0) == 0


def test_using_builtin():
    assert Solution().using_builtin(11) == 3
    assert Solution().using_builtin(128) == 1
    assert Solution().using_builtin(0) == 0


def test_another_version():
    assert Solution().another_version(11) == 3
    assert Solution().another_version(128) == 1
    assert Solution().another_version(0) == 0
