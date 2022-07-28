class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # Dynamic programming. O(n^2)
        LIS = [1] * len(nums)

        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

    def patience_algo(self, nums: list[int]) -> int:
        # BEST. O(n*logn)
        from bisect import bisect_left

        sub: list[int] = []
        for num in nums:
            if not sub or sub[-1] < num:
                sub.append(num)
            else:
                idx = bisect_left(sub, num)
                sub[idx] = num

        return len(sub)

    def submitted_dtl(self, nums: list[int]) -> int:
        # Same idea as patience algo but slower. O(n*m) (m is the length of sub)
        sub: list[int] = []
        for num in nums:
            pos, len_sub = 0, len(sub)
            while pos <= len_sub:
                if pos == len_sub:
                    sub.append(num)
                    break
                elif num <= sub[pos]:
                    sub[pos] = num
                    break
                else:
                    pos += 1

        return len(sub)


def test_length_of_LIS():
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
    assert Solution().lengthOfLIS([1]) == 1


def test_patience_algo():
    assert Solution().patience_algo([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().patience_algo([0, 1, 0, 3, 2, 3]) == 4
    assert Solution().patience_algo([7, 7, 7, 7, 7, 7, 7]) == 1
    assert Solution().patience_algo([1]) == 1


def test_submitted_dtl():
    assert Solution().submitted_dtl([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().submitted_dtl([0, 1, 0, 3, 2, 3]) == 4
    assert Solution().submitted_dtl([7, 7, 7, 7, 7, 7, 7]) == 1
    assert Solution().submitted_dtl([1]) == 1
