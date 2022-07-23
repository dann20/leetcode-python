class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        min_len = min(len(s) for s in strs)
        for pos in range(min_len):
            check = all(strs[idx][pos] == strs[idx + 1][pos] for idx in range(len(strs) - 1))
            if check:
                res += strs[0][pos]
            else:
                break
        return res


def test_longest_common_prefix():
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
