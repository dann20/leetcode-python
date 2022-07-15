class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda item: item[0])

        count = 0
        last_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < last_end:
                count += 1
                last_end = min(end, last_end)
            else:
                last_end = end

        return count


def test_erase_overlap_interval():
    s = Solution()
    assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert s.eraseOverlapIntervals([[1, 3], [2, 4], [3, 5], [4, 9], [8, 10]]) == 2
    assert s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert s.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
