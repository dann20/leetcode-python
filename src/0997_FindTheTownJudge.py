class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # degree_diff = in_degree - out_degree
        # reset to 1-indexed, ignore first 0
        degree_diff = [0] * (n + 1)
        for i, j in trust:
            degree_diff[i] -= 1
            degree_diff[j] += 1

        for idx in range(1, n + 1):
            if degree_diff[idx] == n - 1:
                return idx
        return -1


def test_find_judge():
    assert Solution().findJudge(2, [[1, 2]]) == 2
    assert Solution().findJudge(3, [[1, 3], [2, 3]]) == 3
    assert Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1
