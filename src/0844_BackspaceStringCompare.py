class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def editor(input: str) -> str:
            stack = []
            for c in input:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            return "".join(stack)

        return editor(s) == editor(t)

    def follow_up(self, s: str, t: str) -> bool:
        def gen_next(input: str) -> str:
            skip = 0
            for c in reversed(input):
                if c == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield c

        from itertools import zip_longest
        return all(x == y for x, y in zip_longest(gen_next(s), gen_next(t)))


def test_backspace_compare():
    assert Solution().backspaceCompare("ab#c", "ad#c") is True
    assert Solution().backspaceCompare("ab##", "c#d#") is True
    assert Solution().backspaceCompare("a##c", "#a#c") is True
    assert Solution().backspaceCompare("a#c", "b") is False
    assert Solution().backspaceCompare("xywrrmp", "xywrrm#p") is False


def test_follow_up():
    assert Solution().follow_up("ab#c", "ad#c") is True
    assert Solution().follow_up("ab##", "c#d#") is True
    assert Solution().follow_up("a##c", "#a#c") is True
    assert Solution().follow_up("a#c", "b") is False
    assert Solution().follow_up("xywrrmp", "xywrrm#p") is False
