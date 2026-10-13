class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operation = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: b - a,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(b / a),
        }

        for token in tokens:
            if token in operation:
                a = stack.pop()
                b = stack.pop()
                stack.append(operation[token](a, b))
            else:
                stack.append(int(token))

        return stack.pop()
