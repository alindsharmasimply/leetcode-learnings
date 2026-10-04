class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        count_ones = 0
        count_zeros = 0

        left = right = 0

        max_length = 0

        for right in range(n):
            if nums[right] == 0:
                count_zeros += 1
            elif nums[right] == 1:
                count_ones += 1
            while count_zeros > k:
                if nums[left] == 0:
                    count_zeros -= 1
                elif nums[left] == 1:
                    count_ones -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length
