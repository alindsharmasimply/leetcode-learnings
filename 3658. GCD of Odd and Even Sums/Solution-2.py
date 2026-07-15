from math import gcd


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = int((n / 2) * ((2 * 1) + (n - 1) * 2))
        even_sum = int((n / 2) * ((2 * 2) + (n - 1) * 2))
        return gcd(odd_sum, even_sum)
