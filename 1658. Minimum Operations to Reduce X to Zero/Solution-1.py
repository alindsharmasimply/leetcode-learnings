class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total_sum = sum(nums)

        target = total_sum - x

        if target == 0:
            return len(nums)

        if target < 0:
            return -1

        left = 0
        current_sum = 0
        max_length = -1

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > target:
                current_sum -= nums[left]
                left += 1

            if target == current_sum:
                max_length = max(max_length, right - left + 1)

        return len(nums) - max_length if max_length != -1 else -1
