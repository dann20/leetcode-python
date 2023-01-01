class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # Search row
        top, bot = 0, m - 1
        while top < bot:
            mid = top + (bot - top) // 2
            if target < matrix[mid][0]:
                bot = mid
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break

        if top > bot:
            return False

        # Search position in row
        row = top + (bot - top) // 2
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            if target <= matrix[row][mid]:
                right = mid
            else:
                left = mid + 1
        return True if matrix[row][left] == target else False


def test_search_matrix():
    assert (
        Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
        is True
    )
    assert (
        Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
        is False
    )
