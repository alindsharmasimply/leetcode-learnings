class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        length = len(columnTitle) - 1
        for i, char in enumerate(columnTitle):
            ans += (ord(char) - ord("A") + 1) * (26 ** (length - i))
        return ans
