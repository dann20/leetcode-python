class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n + 1)]
        n_remains = len(players)
        start = 0

        while n_remains > 1:
            start = start + (k % n_remains) - 1
            if start >= n_remains:
                start -= n_remains
            del players[start]
            n_remains = len(players)

            # edge case when deleted player is at the end of the list
            # (prev start = 0, k = n_remains -> current start = -1)
            start = start if start >= 0 else 0

        return players[0]


def test_find_the_winner():
    assert Solution().findTheWinner(5, 2) == 3
    assert Solution().findTheWinner(6, 5) == 1
    assert Solution().findTheWinner(5, 3) == 4
