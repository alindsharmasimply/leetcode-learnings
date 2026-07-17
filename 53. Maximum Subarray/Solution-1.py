import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = int(-math.inf)
        summ = 0
        for num in nums:
            summ = max(num, summ + num)
            ans = max(summ, ans)

        return ans
