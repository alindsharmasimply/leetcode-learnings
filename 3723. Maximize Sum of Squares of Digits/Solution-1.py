class Solution:
    def maxSumOfSquares(self, num: int, summ: int) -> str:
        if num * 9 < summ:
            return ""

        quotient = summ // 9
        remainder = summ % 9

        ans = "9" * quotient

        if remainder:
            ans += str(remainder)

        return ans + ("0" * (num - len(ans)))
