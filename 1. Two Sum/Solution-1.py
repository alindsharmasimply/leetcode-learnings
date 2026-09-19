class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_dict = {}
        for index, num in enumerate(nums):
            second_num = target - num
            if second_num in index_dict:
                return [index_dict[second_num], index]
            index_dict[num] = index
