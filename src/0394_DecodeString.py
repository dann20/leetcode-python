class Solution:
    def decodeString(self, s: str) -> str:
        stack_num = []
        stack_string = []
        cur_string = ""
        cur_num = 0
        for c in s:
            if c == "[":
                stack_string.append(cur_string)
                stack_num.append(cur_num)
                cur_num = 0
                cur_string = ""
            elif c == "]":
                string = stack_string.pop()
                num = stack_num.pop()
                cur_string = string + num * cur_string
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                cur_string += c
        return cur_string


def test_decode_string():
    assert Solution().decodeString("3[a]2[bc]") == "aaabcbc"
    assert Solution().decodeString("3[a2[c]]") == "accaccacc"
    assert Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
