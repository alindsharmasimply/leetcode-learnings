class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        opened = 0
        for char in s:
            if char == "(":
                opened += 1
                max_depth = max(max_depth, opened)
            elif char == ")":
                opened -= 1
        return max_depth
