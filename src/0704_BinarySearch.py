class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1

    def recursive_search(self, nums: list[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.recursive_search(nums, target, left, mid - 1)
        else:
            return self.recursive_search(nums, target, mid + 1, right)

    def using_template(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left if nums[left] == target else -1


def test_search():
    assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1


def test_search_template():
    assert Solution().using_template([-1, 0, 3, 5, 9, 12], 9) == 4
    assert Solution().using_template([-1, 0, 3, 5, 9, 12], 2) == -1


def test_template():
    assert Solution().recursive_search([-1, 0, 3, 5, 9, 12], 9, 0, 5) == 4
    assert Solution().recursive_search([-1, 0, 3, 5, 9, 12], 2, 0, 5) == -1
