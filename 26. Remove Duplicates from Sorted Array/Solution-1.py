class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        swap_pointer = 0
        for num in nums:
            if swap_pointer < 1 or num > nums[swap_pointer - 1]:
                nums[swap_pointer] = num
                swap_pointer += 1
        return swap_pointer
