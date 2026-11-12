from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing_count = 1
        decreasing_count = 1

        ans = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing_count += 1
                decreasing_count = 1
            elif nums[i] < nums[i - 1]:
                increasing_count = 1
                decreasing_count += 1
            else:
                increasing_count = 1
                decreasing_count = 1
            ans = max(ans, increasing_count, decreasing_count)

        return ans
