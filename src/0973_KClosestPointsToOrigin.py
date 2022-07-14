class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        map = dict()
        for idx, point in enumerate(points):
            map[idx] = pow(point[0], 2) + pow(point[1], 2)

        res = []
        count = 0

        for idx, _ in sorted(map.items(), key=lambda item: item[1]):
            res.append(points[idx])
            count += 1
            if count == k:
                break

        return res


def test_k_closest():
    assert Solution().kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]
