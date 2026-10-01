class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        opposing_parenthesis = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in "[{(":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                popped_char = stack.pop()
                if opposing_parenthesis[popped_char] != char:
                    return False
        return len(stack) == 0
