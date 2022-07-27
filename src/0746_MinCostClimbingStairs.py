class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for idx in reversed(range(len(cost) - 2)):
            cost[idx] += min(cost[idx + 1], cost[idx + 2])
        return min(cost[0], cost[1])


def test_min_cost_climbing_stairs():
    assert Solution().minCostClimbingStairs([10, 15, 20]) == 15
    assert Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert Solution().minCostClimbingStairs([10, 15, 20, 25]) == 30
