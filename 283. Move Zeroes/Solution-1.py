class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count], nums[i] = nums[i], nums[count]

                count += 1


# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


# Example 2:

# Input: nums = [0]
# Output: [0]
