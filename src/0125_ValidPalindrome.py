class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alphanumeric(c: str) -> bool:
            return (
                ord("a") <= ord(c) <= ord("z")
                or ord("A") <= ord(c) <= ord("Z")
                or ord("0") <= ord(c) <= ord("9")
            )

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not is_alphanumeric(s[l]):
                l += 1
            while l < r and not is_alphanumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


def test_is_palindrome():
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True
    assert Solution().isPalindrome("race a car") is False
    assert Solution().isPalindrome(" ") is True
