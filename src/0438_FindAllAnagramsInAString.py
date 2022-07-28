class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        p_dict: dict[str, int] = dict()
        sub_dict: dict[str, int] = dict()
        for i in range(len(p)):
            p_dict[p[i]] = p_dict.get(p[i], 0) + 1
            sub_dict[s[i]] = sub_dict.get(s[i], 0) + 1

        res = [0] if p_dict == sub_dict else []
        begin = 0
        for end in range(len(p), len(s)):
            sub_dict[s[end]] = sub_dict.get(s[end], 0) + 1
            sub_dict[s[begin]] -= 1
            if sub_dict[s[begin]] == 0:
                sub_dict.pop(s[begin])
            begin += 1
            if p_dict == sub_dict:
                res.append(begin)

        return res


def test_find_anagrams():
    assert Solution().findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert Solution().findAnagrams("abab", "ab") == [0, 1, 2]
