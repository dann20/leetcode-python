class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1

        while 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True

        return False


def test_search_matrix():
    s = Solution()
    assert (
        s.searchMatrix(
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            5,
        )
        is True
    )

    assert (
        s.searchMatrix(
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            20,
        )
        is False
    )
