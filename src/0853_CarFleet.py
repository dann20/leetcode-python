class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        stack: list[float] = []
        for p, s in cars:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


def test_car_fleet():
    assert (
        Solution().carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3])
        == 3
    )
    assert Solution().carFleet(target=10, position=[3], speed=[3]) == 1
    assert Solution().carFleet(target=100, position=[0, 2, 4], speed=[4, 2, 1]) == 1
