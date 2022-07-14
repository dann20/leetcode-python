class Solution:
    def frequencySort(self, s: str) -> str:
        map = dict()
        for c in s:
            map[c] = map.get(c, 0) + 1

        res = ""
        for char, freq in sorted(map.items(), key=lambda item: item[1], reverse=True):
            res += char * freq

        return res


def test_frequency_sort():
    assert Solution().frequencySort("tree") == "eetr"
    assert Solution().frequencySort("cccaaa") == "cccaaa"
    assert Solution().frequencySort("Aabb") == "bbAa"
