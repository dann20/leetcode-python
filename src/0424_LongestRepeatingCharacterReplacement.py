class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq_tbl = {}
        left = 0
        max_freq = 0
        for right in range(len(s)):
            freq_tbl[s[right]] = freq_tbl.get(s[right], 0) + 1
            max_freq = max(max_freq, freq_tbl[s[right]])
            if not (right - left + 1 - max_freq <= k):
                freq_tbl[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res


def test_character_replacement():
    assert Solution().characterReplacement("ABSDASAAACABBABBABA", 6) == 13
    assert Solution().characterReplacement("AAAB", 0) == 3
    assert Solution().characterReplacement("ABAB", 2) == 4
    assert Solution().characterReplacement("AAAA", 2) == 4
    assert Solution().characterReplacement("AAAA", 0) == 4
    assert Solution().characterReplacement("AABABBA", 1) == 4
