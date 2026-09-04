from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_length = 0
        for item in s:
            if item - 1 not in s:
                length = 1
                while (item + length) in s:
                    length += 1
                max_length = max(max_length, length)
        return max_length
