class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(row: int, col: int) -> None:
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != "1":
                return
            grid[row][col] = "#"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res


def test_num_islands():
    assert (
        Solution().numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"]])
        == 1
    )
    assert (
        Solution().numIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    assert (
        Solution().numIslands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
