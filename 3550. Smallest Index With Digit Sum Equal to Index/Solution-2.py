from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        return next(
            (i for i, num in enumerate(nums) if i == self._sum_of_digits(num)), -1
        )

    def _sum_of_digits(self, x: int):
        return sum(int(digit) for digit in str(x))
