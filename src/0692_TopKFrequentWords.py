class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        from heapq import nsmallest
        from collections import Counter

        freqs = Counter(words)
        heap = (nsmallest(k, freqs.items(), key=lambda item: (-item[1], item[0])))
        return [word for word, _ in heap]


def test_top_k_frequent():
    assert Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
    assert Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) == ["the", "is", "sunny", "day"]
