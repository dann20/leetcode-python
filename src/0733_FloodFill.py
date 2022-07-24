class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        m, n = len(image), len(image[0])
        origin = image[sr][sc]
        visited = set()

        def dfs(row: int, col: int):
            if (
                row < 0
                or row >= m
                or col < 0
                or col >= n
                or (row, col) in visited
                or image[row][col] != origin
            ):
                return
            if image[row][col] == origin:
                image[row][col] = color
                visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        dfs(sr, sc)
        return image


def test_flood_fill():
    assert Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]
    assert Solution().floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1) == [
        [0, 0, 0],
        [0, 1, 1],
    ]
    assert Solution().floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [
        [0, 0, 0],
        [0, 0, 0],
    ]
