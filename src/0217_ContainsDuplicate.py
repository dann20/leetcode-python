class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False


def test_contains_duplicate():
    assert Solution().containsDuplicate([1, 2, 3, 1]) is True
    assert Solution().containsDuplicate([1, 2, 3, 4]) is False
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
