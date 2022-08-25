class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev_num = 0
        result = 0
        for c in s:
            cur_num = roman_dict[c]
            result += cur_num
            if cur_num > prev_num:
                result -= 2 * prev_num
            prev_num = cur_num
        return result


def test_roman_to_int():
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("IV") == 4
    assert Solution().romanToInt("IX") == 9
    assert Solution().romanToInt("LVIII") == 58
    assert Solution().romanToInt("MCMXCIV") == 1994
    assert Solution().romanToInt("MMXIV") == 2014
    assert Solution().romanToInt("MMXIX") == 2019
