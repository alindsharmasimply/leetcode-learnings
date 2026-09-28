class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                max_depth = max(max_depth, len(stack))
                stack.pop()
        return max_depth
