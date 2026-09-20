class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = 0
        for index, char in enumerate(s):
            degree += (index + 1) * abs(ord(char) - 123)
        return degree
