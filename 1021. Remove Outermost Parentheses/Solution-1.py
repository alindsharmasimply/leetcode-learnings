class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        last_primitive_start = 0
        result = []

        left = right = 0

        for i, char in enumerate(s):
            if char == "(":
                left += 1
            else:
                right += 1

            if left == right:
                result.append(s[last_primitive_start + 1 : i])
                left = right = 0
                last_primitive_start = i + 1

        return "".join(result)
