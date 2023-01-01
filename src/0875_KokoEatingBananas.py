class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        import math

        max_bananas = max(piles)
        left, right = 1, max_bananas
        res = max_bananas

        while left < right:
            mid = left + (right - left) // 2

            total_time = 0
            for num_bananas in piles:
                total_time += math.ceil(num_bananas / mid)

            if total_time <= h:
                res = min(mid, res)
                right = mid
            else:
                left = mid + 1

        return res


def test_min_eating_speed():
    assert Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8) == 4
    assert Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5) == 30
    assert Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6) == 23
