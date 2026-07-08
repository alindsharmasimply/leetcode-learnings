from typing import List
import sys


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        result = []
        sys.set_int_max_str_digits(0)

        def concat_and_mul(s: str) -> int:
            concat_str = ""
            sum = 0
            for char in s:
                num = int(char)
                if num != 0:
                    concat_str += char
                sum += num
            return (int(concat_str if concat_str else 0) * sum) % (10**9 + 7)

        for query in queries:
            sub = s[query[0] : query[1] + 1]
            result.append(concat_and_mul(sub))

        return result
