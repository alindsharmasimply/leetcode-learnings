class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        min_length = len(nums) + 1
        current_sum = 0

        for right, num in enumerate(nums):
            current_sum += num
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if min_length == len(nums) + 1 else min_length
