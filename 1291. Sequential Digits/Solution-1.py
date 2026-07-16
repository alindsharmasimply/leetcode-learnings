from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        for length in range(2, 10):
            for i in range(10 - length):
                n = int(digits[i : i + length])
                if low <= n <= high:
                    result.append(n)
        return result
