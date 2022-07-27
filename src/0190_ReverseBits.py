class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1
            res |= n & 1
            n >>= 1
        return res

    def optimal(self, n: int) -> int:
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n

    def string_manipulation(self, n: int) -> int:
        return int(f'{n:032b}'[::-1], 2)


def test_optimal():
    assert Solution().optimal(0) == 0
    assert Solution().optimal(43261596) == 964176192
    assert Solution().optimal(4294967293) == 3221225471


def test_reverse_bits():
    assert Solution().reverseBits(0) == 0
    assert Solution().reverseBits(43261596) == 964176192
    assert Solution().reverseBits(4294967293) == 3221225471


def test_string_manipulation():
    assert Solution().string_manipulation(0) == 0
    assert Solution().string_manipulation(43261596) == 964176192
    assert Solution().string_manipulation(4294967293) == 3221225471
