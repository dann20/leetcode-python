class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1], [1, 1]]
        if numRows <= 2:
            return res[:numRows]

        for i in range(2, numRows):
            res.append([1] + [res[i - 1][j] + res[i - 1][j + 1] for j in range(i - 1)] + [1])
        return res


def test_generate():
    assert Solution().generate(0) == []
    assert Solution().generate(1) == [[1]]
    assert Solution().generate(2) == [[1], [1, 1]]
    assert Solution().generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
