class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict

        res: dict[str, list[str]] = defaultdict(list)
        for string in strs:
            sorted_string = str(sorted(string))
            res[sorted_string].append(string)
        return list(res.values())


def test_group_anagrams():
    assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]
    assert Solution().groupAnagrams([""]) == [[""]]
    assert Solution().groupAnagrams(["a"]) == [["a"]]
