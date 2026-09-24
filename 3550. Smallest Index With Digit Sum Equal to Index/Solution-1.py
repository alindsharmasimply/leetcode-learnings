from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_of_digits(x: int):
            sum = 0
            while x != 0:
                sum += x % 10
                x //= 10
            return sum

        for i, num in enumerate(nums):
            if i == sum_of_digits(num):
                return i
        return -1
