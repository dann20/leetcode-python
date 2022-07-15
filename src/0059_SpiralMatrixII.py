class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        if n == 0:
            return []
        matrix = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(1, n * n + 1):
            matrix[i][j] = k
            if matrix[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return matrix


def test_generate_matrix():
    s = Solution()
    assert s.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert s.generateMatrix(1) == [[1]]
    assert s.generateMatrix(0) == []
