class Solution:
    # Iterative bottom-up with const memory
    def rob(self, nums: list[int]) -> int:
        # order: prev2, prev1, num
        prev2, prev1 = 0, 0
        for num in nums:
            tmp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = tmp
        return prev1


class Opt3:
    # Iterative bottom-up with memoization
    def rob(self, nums: list[int]) -> int:
        length = len(nums)
        memo = [0] * (length + 1)
        memo[0] = 0
        memo[1] = nums[0]
        for idx in range(1, length):
            memo[idx + 1] = max(memo[idx], memo[idx - 1] + nums[idx])
        return memo[-1]


class Opt2:
    # Recursive top-down with memoization
    def rob(self, nums: list[int]) -> int:
        self.cache = {}

        def rob_step(house: int) -> int:
            if house < 0:
                return 0
            elif house not in self.cache:
                self.cache[house] = max(rob_step(house - 2) + nums[house], rob_step(house - 1))
            return self.cache[house]

        return rob_step(len(nums) - 1)


class Opt1:
    # Recursive top-down
    def rob(self, nums: list[int]) -> int:
        def rob_step(house: int) -> int:
            if house < 0:
                return 0
            return max(rob_step(house - 2) + nums[house], rob_step(house - 1))

        return rob_step(len(nums) - 1)


def test_opt1():
    assert Opt1().rob([1, 2, 3, 1]) == 4
    assert Opt1().rob([2, 7, 9, 3, 1]) == 12
    assert Opt1().rob([2, 1, 1, 2]) == 4


def test_opt2():
    assert Opt2().rob([1, 2, 3, 1]) == 4
    assert Opt2().rob([2, 7, 9, 3, 1]) == 12
    assert Opt2().rob([2, 1, 1, 2]) == 4


def test_opt3():
    assert Opt3().rob([1, 2, 3, 1]) == 4
    assert Opt3().rob([2, 7, 9, 3, 1]) == 12
    assert Opt3().rob([2, 1, 1, 2]) == 4


def test_rob():
    assert Solution().rob([1, 2, 3, 1]) == 4
    assert Solution().rob([2, 7, 9, 3, 1]) == 12
    assert Solution().rob([2, 1, 1, 2]) == 4
