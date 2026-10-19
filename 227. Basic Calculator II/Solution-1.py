class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        n = len(s)
        sign = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                num = (num * 10) + int(char)

            if (not char.isdigit() and char != " ") or (i == n - 1):
                if sign == "+":
                    stack.append(num)
                if sign == "-":
                    stack.append(-num)
                if sign == "*":
                    stack.append(stack.pop() * num)
                if sign == "/":
                    stack.append(int(stack.pop() / num))

                sign = char
                num = 0

        return sum(stack)
