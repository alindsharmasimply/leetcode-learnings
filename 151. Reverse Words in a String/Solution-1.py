class Solution:
    def reverseWords(self, s: str) -> str:
        # Remember, split() function by default splits at any whitespace as a delimiter
        return " ".join(reversed(s.split()))
