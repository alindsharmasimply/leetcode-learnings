class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        sorted_half = sorted(s[: n // 2])
        return "".join(
            sorted_half + ([s[n // 2]] if n % 2 != 0 else []) + sorted_half[::-1]
        )
