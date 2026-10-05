class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefix_sum = 0
        total_sum = sum(nums)  # O(n)

        for i, num in enumerate(nums):
            if prefix_sum == total_sum - prefix_sum - num:
                return i
            prefix_sum += num

        return -1
