class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 0, 1, 2, 3, 4
        dp = [[], [1, 1, 1, 1, 1]]
        mod = 10 ** 9 + 7

        for j in range(2, n + 1):
            dp.append([1, 1, 1, 1, 1])
            dp[j][a] = (dp[j - 1][e] + dp[j - 1][i] + dp[j - 1][u]) % mod
            dp[j][e] = (dp[j - 1][a] + dp[j - 1][i]) % mod
            dp[j][i] = (dp[j - 1][e] + dp[j - 1][o]) % mod
            dp[j][o] = dp[j - 1][i]
            dp[j][u] = (dp[j - 1][i] + dp[j - 1][o]) % mod
        return sum(dp[n]) % mod

    def constant_mem(self, n: int) -> int:
        a, e, i, o, u = 0, 1, 2, 3, 4
        prev = []
        dp = [1, 1, 1, 1, 1]
        mod = 10 ** 9 + 7

        for _ in range(n - 1):
            prev = dp.copy()
            dp[a] = (prev[e] + prev[i] + prev[u]) % mod
            dp[e] = (prev[a] + prev[i]) % mod
            dp[i] = (prev[e] + prev[o]) % mod
            dp[o] = prev[i]
            dp[u] = (prev[i] + prev[o]) % mod
        return sum(dp) % mod


def test_count_vowel_permutation():
    assert Solution().countVowelPermutation(1) == 5
    assert Solution().countVowelPermutation(2) == 10
    assert Solution().countVowelPermutation(3) == 19
    assert Solution().countVowelPermutation(4) == 35
    assert Solution().countVowelPermutation(5) == 68
    assert Solution().countVowelPermutation(6) == 129


def test_constant_mem():
    assert Solution().constant_mem(1) == 5
    assert Solution().constant_mem(2) == 10
    assert Solution().constant_mem(3) == 19
    assert Solution().constant_mem(4) == 35
    assert Solution().constant_mem(5) == 68
    assert Solution().constant_mem(6) == 129
