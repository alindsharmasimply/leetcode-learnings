import collections
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # Case 1: k equals the length of the array
        if len(nums) == k:
            return max(nums)

        counts = collections.Counter(nums)

        # Case 2: k equals 1
        if k == 1:
            unique_elements = [num for num, count in counts.items() if count == 1]
            return max(unique_elements) if unique_elements else -1

        # Case 3: 1 < k < n
        # Only the first or last elements can belong to exactly one subarray.
        # Any middle element will always be included in multiple subarrays.
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans
