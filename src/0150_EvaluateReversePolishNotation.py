class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == "+":
                    local_res = operand1 + operand2
                elif token == "-":
                    local_res = operand1 - operand2
                elif token == "*":
                    local_res = operand1 * operand2
                elif token == "/":
                    local_res = int(operand1 / operand2)
                else:
                    raise NotImplementedError
                stack.append(local_res)
        return stack.pop()


def test_eval_RPN():
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert (
        Solution().evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
        == 22
    )
