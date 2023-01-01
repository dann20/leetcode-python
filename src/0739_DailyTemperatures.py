class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack: list[tuple[int, int]] = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][-1]:
                prev_day = stack.pop()
                res[prev_day[0]] = idx - prev_day[0]
            stack.append((idx, temp))

        return res


def test_daily_temperatures():
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]
    assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert Solution().dailyTemperatures([30, 60, 90]) == [1, 1, 0]
