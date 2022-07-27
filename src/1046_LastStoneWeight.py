class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        from heapq import heapify, heappop, heappush

        stones = [-stone for stone in stones]
        heapify(stones)
        while len(stones) > 1:
            first = heappop(stones)
            second = heappop(stones)
            new_stone = first - second
            if new_stone:
                heappush(stones, new_stone)
        return -stones[0] if stones else 0


def test_last_stone_weight():
    assert Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert Solution().lastStoneWeight([2, 7, 4, 1, 8, 1, 1]) == 0
    assert Solution().lastStoneWeight([1]) == 1
