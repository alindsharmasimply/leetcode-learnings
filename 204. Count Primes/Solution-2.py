class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        return sum(self._sieve_of_eratosthenes(n))

    def _sieve_of_eratosthenes(self, n: int) -> list[bool]:
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return is_prime
