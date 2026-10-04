class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        count = {0: -1}
        prefix = 0

        for current_index in range(len(nums)):
            prefix += nums[current_index]
            if k != 0:
                prefix %= k
            if prefix in count:
                if current_index - count[prefix] > 1:
                    return True
            else:
                count[prefix] = current_index

        return False
