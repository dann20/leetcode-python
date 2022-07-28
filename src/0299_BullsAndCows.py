class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        count = [0] * 10
        for s_str, g_str in zip(secret, guess):
            s, g = int(s_str), int(g_str)
            if s == g:
                bulls += 1
            else:
                if count[s] < 0:
                    cows += 1
                if count[g] > 0:
                    cows += 1
                count[s] += 1
                count[g] -= 1

        return f"{bulls}A{cows}B"


def test_get_hint():
    assert Solution().getHint("1807", "7810") == "1A3B"
    assert Solution().getHint("1123", "0111") == "1A1B"
