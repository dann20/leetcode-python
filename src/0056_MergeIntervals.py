class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda interval: interval[0])

        res = [intervals[0]]
        last_start, last_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= last_end:
                new_end = max(end, last_end)
                res[-1] = [last_start, new_end]
                last_end = new_end
            else:
                res.append([start, end])
                last_start, last_end = start, end

        return res


def test_merge():
    assert Solution().merge([[1, 3], [6, 7], [2, 6], [8, 10], [19, 30], [15, 18]]) == [[1, 7], [8, 10], [15, 18], [19, 30]]
    assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert Solution().merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert Solution().merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
