import math
from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int | float:
        ans = math.inf

        for window_size in range(l, r + 1):
            window_sum = sum(nums[:window_size])

            if window_sum > 0:
                ans = min(ans, window_sum)

            for i in range(window_size, len(nums)):
                window_sum -= nums[i - window_size]
                window_sum += nums[i]

                if window_sum > 0:
                    ans = min(ans, window_sum)

        return ans if ans != math.inf else -1
