class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        mid = len(x) // 2
        for idx in range(mid):
            if x[idx] != x[len(x) - 1 - idx]:
                return False
        return True


def test_is_palinedrome():
    assert Solution().isPalindrome(121) is True
    assert Solution().isPalindrome(-121) is False
    assert Solution().isPalindrome(10) is False
    assert Solution().isPalindrome(1876556781) is True
    assert Solution().isPalindrome(13331) is True
    assert Solution().isPalindrome(125125) is False
