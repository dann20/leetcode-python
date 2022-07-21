class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if not target:
            return len(nums)

        max_len = 0
        cur_sum = 0
        prefix = {0: 0}

        for idx, num in enumerate(nums):
            cur_sum += num
            remains = cur_sum - target
            new_len = idx + 1 - prefix.get(remains, idx + 1)
            max_len = max(max_len, new_len)
            prefix[cur_sum] = idx + 1

        return len(nums) - max_len if max_len else -1


def test_min_operations():
    assert Solution().minOperations([1, 2, 3], 3) == 1
    assert Solution().minOperations([1, 1, 4, 2, 3], 5) == 2
    assert Solution().minOperations([3, 2, 20, 1, 1, 3], 10) == 5
    assert Solution().minOperations([5, 6, 7, 8, 9], 4) == -1
