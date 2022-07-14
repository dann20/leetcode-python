class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from heapq import heapify, heappop

        map = dict()
        for num in nums:
            map[num] = map.get(num, 0) + 1

        res = []
        max_heap_freq = [-freq for freq in map.values()]
        heapify(max_heap_freq)

        for _ in range(k):
            # basically, heappop to get next max freq, use that freq as value to find key in hash_map
            next_max_freq = -heappop(max_heap_freq)
            next_num = list(map.keys())[list(map.values()).index(next_max_freq)]
            map.pop(next_num, None)
            res.append(next_num)

        return res


def test_top_k_frequent():
    assert Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert Solution().topKFrequent([1], 1) == [1]
    assert Solution().topKFrequent([1, 2], 2) == [1, 2]
