class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums.sort(key=lambda x: x * x)

        score = 0

        n = len(nums)

        for i, num in enumerate(nums):
            if (i + 1) <= (n // 2):
                score -= num * num
            else:
                score += num * num

        return score
