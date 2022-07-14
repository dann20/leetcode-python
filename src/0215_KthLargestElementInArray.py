class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(l, r):
            pivot, p = nums[r], l
            for idx in range(l, r):
                if nums[idx] <= pivot:
                    nums[idx], nums[p] = nums[p], nums[idx]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quick_select(l, p - 1)
            elif p < k:
                return quick_select(p + 1, r)
            else:
                return nums[p]

        return quick_select(0, len(nums) - 1)

    def use_heapq(self, nums: list[int], k: int) -> int:
        from heapq import heapify, heappop
        from random import shuffle

        shuffle(nums)
        nums = [-num for num in nums]
        heapify(nums)
        res = 0
        for _ in range(k):
            res = heappop(nums)
        return -res

    def simple(self, nums: list[int], k: int) -> int:
        nums.sort()
        return nums[-k]


def test_find_kth_largest():
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_use_heapq():
    assert Solution().use_heapq([3, 2, 1, 5, 6, 4], 2) == 5
    assert Solution().use_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_simple():
    assert Solution().simple([3, 2, 1, 5, 6, 4], 2) == 5
    assert Solution().simple([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
