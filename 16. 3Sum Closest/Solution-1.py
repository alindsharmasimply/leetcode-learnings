class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]

                # If we find an exact match, it's impossible to get closer. Return immediately.
                if summ == target:
                    return summ
                if abs(summ - target) < abs(ans - target):
                    ans = summ
                if summ < target:
                    left += 1
                else:
                    right -= 1
        return ans
