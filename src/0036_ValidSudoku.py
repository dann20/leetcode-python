class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        from collections import defaultdict

        rows: dict[int, set[str]] = defaultdict(set)
        cols: dict[int, set[str]] = defaultdict(set)
        sub_boxes: dict[tuple[int, int], set[str]] = defaultdict(set)
        for row_idx in range(9):
            for col_idx in range(9):
                element = board[row_idx][col_idx]
                if element == ".":
                    continue
                if (
                    element in rows[row_idx]
                    or element in cols[col_idx]
                    or element in sub_boxes[(row_idx // 3, col_idx // 3)]
                ):
                    return False
                rows[row_idx].add(element)
                cols[col_idx].add(element)
                sub_boxes[(row_idx // 3, col_idx // 3)].add(element)
        return True


def test_valid_sudoku():
    assert (
        Solution().isValidSudoku(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
        is True
    )

    assert (
        Solution().isValidSudoku(
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
        is False
    )
