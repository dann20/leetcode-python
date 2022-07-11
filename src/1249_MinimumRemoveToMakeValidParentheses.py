class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        list_chars = list(s)
        p_open = list()
        p_close = list()

        for idx, c in enumerate(list_chars):
            if c == "(":
                p_open.append(idx)
            elif c == ")":
                if p_open:
                    p_open.pop()
                else:
                    p_close.append(idx)

        for idx in sorted(p_open + p_close, reverse=True):
            del list_chars[idx]
        return "".join(list_chars)


def test_min_remove_to_make_valid():
    assert Solution().minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
    assert Solution().minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
    assert Solution().minRemoveToMakeValid("))((") == ""
