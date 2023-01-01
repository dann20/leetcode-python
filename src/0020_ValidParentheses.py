class Solution:
    def isValid(self, s: str) -> bool:
        map: dict[str, str] = {")": "(", "}": "{", "]": "["}
        stack: list[str] = []
        for c in s:
            if c in map:
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack


def test_is_valid():
    assert Solution().isValid("()") is True
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("(]") is False
    assert Solution().isValid("]") is False
