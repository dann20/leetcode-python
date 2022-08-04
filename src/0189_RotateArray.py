class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        def reverse(nums: list[int], start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)

    def simple(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


def test_rotate():
    s = Solution()
    list1 = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(list1, 3)
    assert list1 == [5, 6, 7, 1, 2, 3, 4]

    list2 = [-1, -100, 3, 99]
    s.rotate(list2, 2)
    assert list2 == [3, 99, -1, -100]


def test_simple():
    s = Solution()
    list1 = [1, 2, 3, 4, 5, 6, 7]
    s.simple(list1, 3)
    assert list1 == [5, 6, 7, 1, 2, 3, 4]

    list2 = [-1, -100, 3, 99]
    s.simple(list2, 2)
    assert list2 == [3, 99, -1, -100]
