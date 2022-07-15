class Solution:
    def sortColors(self, nums: list[int]) -> None:
        idx = 0
        end = len(nums)
        while idx < end:
            if nums[idx] == 2:
                nums.append(nums.pop(idx))
                end -= 1
            elif nums[idx] == 0:
                nums.insert(0, nums.pop(idx))
                idx += 1
            else:
                idx += 1


def test_sort_colors():
    input1 = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(input1)
    assert input1 == [0, 0, 1, 1, 2, 2]

    input2 = [2, 0, 1]
    Solution().sortColors(input2)
    assert input2 == [0, 1, 2]
