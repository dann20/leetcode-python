class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter

        ans = 0
        flag = True
        for v in Counter(s).values():
            if v % 2 == 1:
                ans += v if flag else v - 1
                flag = False
            else:
                ans += v

        return ans


def test_longest_palindrome():
    assert Solution().longestPalindrome("abccccdd") == 7
    assert Solution().longestPalindrome("babad") == 5
    assert Solution().longestPalindrome("aaabbbccccddef") == 11
    assert Solution().longestPalindrome("a") == 1
