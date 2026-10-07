class Solution:
    def countPrimes(self, n: int) -> int:

        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            i = 2
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 1
            return True

        count = 0
        n -= 1
        while n >= 2:
            count += 1 if is_prime(n) else 0
            n -= 1

        return count
