from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = Counter(s)
        for character in t:
            if character not in count or count[character] <= 0:
                return False
            count[character] -= 1

        return True
