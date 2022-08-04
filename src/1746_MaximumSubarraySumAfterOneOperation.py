class Solution:
    def maximum_subarray_sum_after_one_operation(self, nums: list[int]) -> int:
        def max_sum(arr: list[int]) -> list[int]:
            """
            Get max sum of subarray ended with element idx
            """
            res = [0] * len(arr)
            cur_sum = 0
            for i, num in enumerate(arr):
                cur_sum += num
                if cur_sum > num:
                    res[i] = cur_sum
                else:
                    res[i] = num
                cur_sum = res[i]
            return res

        track_forward = [0] + max_sum(nums)
        track_backward = list(reversed(max_sum(list(reversed(nums))))) + [0]

        res = [0] * len(nums)
        for i in range(len(res)):
            tmp = nums[i] * nums[i]
            res[i] = max(
                track_forward[i] + tmp,
                track_backward[i + 1] + tmp,
                track_forward[i] + track_backward[i + 1] + tmp,
            )

        return max(res)


def test_maximum_subarray_sum_after_one_operation():
    assert Solution().maximum_subarray_sum_after_one_operation([2, -1, -4, -3]) == 17
    assert (
        Solution().maximum_subarray_sum_after_one_operation([1, -1, 1, 1, -1, -1, 1])
        == 4
    )
    assert Solution().maximum_subarray_sum_after_one_operation(
        [1, -2, 3, 1, 2, -6, 2, 4, -5, 6, -7]
    ) == 56
