class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res: list[str] = []
        stack: list[str] = []

        def backtrack(num_opens: int, num_closes: int) -> None:
            if num_opens == num_closes == n:
                res.append("".join(stack))
                return

            if num_opens < n:
                stack.append("(")
                backtrack(num_opens + 1, num_closes)
                stack.pop()

            if num_closes < num_opens:
                stack.append(")")
                backtrack(num_opens, num_closes + 1)
                stack.pop()

        backtrack(0, 0)
        return res


def test_generate_parenthesis():
    assert Solution().generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]
    assert Solution().generateParenthesis(1) == ["()"]
