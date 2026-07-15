class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = (n / 2) * ((2 * 1) + (n - 1) * 2)
        even_sum = (n / 2) * ((2 * 2) + (n - 1) * 2)

        def get_gcd(a, b):
            if b == 0:
                return a
            return get_gcd(b, a % b)

        return int(get_gcd(odd_sum, even_sum))
