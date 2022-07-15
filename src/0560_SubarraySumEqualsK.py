class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_map = {0: 1}
        cur_sum = 0
        count = 0

        for num in nums:
            cur_sum += num
            remains = cur_sum - k
            count += prefix_map.get(remains, 0)
            prefix_map[cur_sum] = prefix_map.get(cur_sum, 0) + 1

        return count


def test_subarray_sum():
    s = Solution()
    assert s.subarraySum([1, 1, 1], 2) == 2
    assert s.subarraySum([1, 2, 3], 3) == 2
