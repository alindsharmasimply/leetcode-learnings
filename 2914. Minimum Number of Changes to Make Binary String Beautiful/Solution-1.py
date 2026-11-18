class Solution:
    def minChanges(self, s: str) -> int:
        summ = 0
        for a, b in zip(s[::2], s[1::2]):
            if a != b:
                summ += 1
        return summ