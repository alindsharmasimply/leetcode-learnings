class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(max_possible_target_sum: int):
            current_sum = 0
            total_subarrays = 1
            for num in nums:
                if current_sum + num > max_possible_target_sum:
                    total_subarrays += 1
                    current_sum = num
                    if total_subarrays > k:
                        return False
                else:
                    current_sum += num
            return True

        low = max(nums)
        high = sum(nums)
        ans = high

        while low <= high:
            mid = low + (high - low) // 2

            if can_split(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
