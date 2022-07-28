class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0 for _ in range(26)]
        for c in s:
            counts[ord(c) - 97] += 1
        for c in t:
            counts[ord(c) - 97] -= 1
        return not any(counts)


def test_is_anagram():
    assert Solution().isAnagram("anagram", "nagaram") is True
    assert Solution().isAnagram("rat", "car") is False
