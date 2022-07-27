from typing import Callable


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def condition(asc: bool = True) -> Callable[[list[int], int], bool]:
            if asc:
                return lambda arr, k: arr[k] >= target
            else:
                return lambda arr, k: arr[k] <= target

        def binary_search(arr: list[int], asc: bool = True) -> int:
            cond = condition(asc)
            left, right = 0, len(arr) - 1
            while left < right:
                mid = left + (right - left) // 2
                if cond(arr, mid):
                    right = mid
                else:
                    left = mid + 1
            return left if arr[left] == target else -1

        res: list[int] = [-1, -1]

        if not nums:
            return res

        res[0] = binary_search(nums, True)
        if res[0] != -1:
            res[1] = len(nums) - 1 - binary_search(nums[::-1], False)

        return res


def test_search_range():
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert Solution().searchRange([], 0) == [-1, -1]
