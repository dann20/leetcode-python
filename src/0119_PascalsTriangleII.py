class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        prev_row = self.getRow(rowIndex - 1)
        row = [1]
        for idx in range(rowIndex - 1):
            row.append(prev_row[idx] + prev_row[idx + 1])
        return row + [1]


def test_get_row():
    assert Solution().getRow(0) == [1]
    assert Solution().getRow(1) == [1, 1]
    assert Solution().getRow(2) == [1, 2, 1]
    assert Solution().getRow(3) == [1, 3, 3, 1]
    assert Solution().getRow(5) == [1, 5, 10, 10, 5, 1]
