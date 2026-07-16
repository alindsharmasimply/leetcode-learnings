class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def get_gcd(a, b):
            if b == 0:
                return a
            return get_gcd(b, a % b)

        mx = [0] * (len(nums) + 1)
        prefixGcd = [0] * len(nums)
        for idx, num in enumerate(nums):
            mx[idx + 1] = max(num, mx[idx])
            prefixGcd[idx] = get_gcd(num, mx[idx + 1])
        prefixGcd.sort()
        l, r = 0, len(prefixGcd) - 1
        sum = 0
        while l < r:
            sum += get_gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1
        return sum
