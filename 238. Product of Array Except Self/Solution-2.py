class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        result = [1] * n

        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        suffix_product = 1

        for i in reversed(range(n)):
            result[i] = result[i] * suffix_product
            suffix_product *= nums[i]

        return result
