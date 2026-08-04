from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        result = []
        min_num, max_num = min(nums), max(nums)
        for x in range(min_num + 1, max_num):
            if x not in num_set:
                result.append(x)
        return result
