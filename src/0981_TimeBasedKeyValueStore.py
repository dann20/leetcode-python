from collections import defaultdict


class TimeMap:
    def __init__(self) -> None:
        self.data: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:  # noqa: A003
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        data = self.data[key]
        len_data = len(data)

        left, right = 0, len_data - 1
        while left < right:
            mid = left + (right - left) // 2
            if data[mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1

        if left >= 1 and data[left][0] > timestamp:
            return data[left - 1][1]
        if left == len_data - 1:
            return data[left][1]
        return ""


def test_time_map() -> None:
    time_map = TimeMap()

    time_map.set("foo", "bar", 1)
    assert time_map.get("foo", 1) == "bar"
    assert time_map.get("foo", 3) == "bar"

    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 4) == "bar2"
    assert time_map.get("foo", 5) == "bar2"
