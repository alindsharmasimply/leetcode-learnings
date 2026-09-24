from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_length = 0
        for item in seen:
            if item - 1 not in seen:
                length = 1
                while (item + length) in seen:
                    length += 1
                max_length = max(max_length, length)
        return max_length
