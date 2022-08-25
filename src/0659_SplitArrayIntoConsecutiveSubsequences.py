class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        from collections import Counter

        left = Counter(nums)
        end: dict[int, int] = Counter()

        for num in nums:
            if not left[num]:
                continue
            left[num] -= 1

            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
            elif left[num + 1] and left[num + 2]:
                left[num + 1] -= 1
                left[num + 2] -= 1
                end[num + 2] += 1
            else:
                return False

        return True


def test_is_possible():
    assert Solution().isPossible([1, 2, 3, 3, 4, 5]) is True
    assert Solution().isPossible([1, 2, 3, 3, 4, 4, 5, 5]) is True
    assert Solution().isPossible([1, 2, 3, 4, 4, 5]) is False
