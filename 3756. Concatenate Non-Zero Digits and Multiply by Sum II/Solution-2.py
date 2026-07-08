from typing import List
import sys


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        result = []
        n = len(s)
        MOD = 10**9 + 7
        sys.set_int_max_str_digits(0)
        prefix_sum = [0] * n
        prefix_valid_num = [0] * n
        prefix_valid_count = [0] * n

        d = int(s[0])
        prefix_sum[0] = d
        prefix_valid_num[0] = d if d != 0 else 0
        prefix_valid_count[0] = 1 if d != 0 else 0

        for i in range(1, n):
            d = int(s[i])
            prefix_sum[i] = (prefix_sum[i - 1] + d) % MOD
            prefix_valid_num[i] = (
                ((prefix_valid_num[i - 1] * 10) + d) % MOD
                if d != 0
                else prefix_valid_num[i - 1]
            )
            prefix_valid_count[i] = prefix_valid_count[i - 1] + (1 if d != 0 else 0)

        for l, r in queries:
            sum = (prefix_sum[r] - (prefix_sum[l - 1] if l - 1 >= 0 else 0)) % MOD
            non_zero_digits = prefix_valid_count[r] - (
                prefix_valid_count[l - 1] if l - 1 >= 0 else 0
            )
            valid_num = (
                prefix_valid_num[r]
                - (
                    prefix_valid_num[l - 1] * pow(10, non_zero_digits, MOD)
                    if l - 1 >= 0
                    else 0
                )
            ) % MOD
            result.append((sum * valid_num) % MOD)

        return result
