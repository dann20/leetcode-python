class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        def search(visited: set, keys: list[int]):
            for key in keys:
                if key not in visited:
                    visited.add(key)
                    search(visited, rooms[key])

        visited = {0}
        search(visited, rooms[0])
        if visited == set(i for i in range(len(rooms))):
            return True
        return False


def test_can_visit_all_rooms():
    assert Solution().canVisitAllRooms([[1], [2], [3], []]) is True
    assert Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) is False
