class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans = nums[0]

        current_min = 1
        current_max = 1

        for num in nums:
            if num < 0:
                current_min, current_max = current_max, current_min

            current_min = min(num, current_min * num)
            current_max = max(num, current_max * num)

            ans = max(ans, current_max)

        return ans
