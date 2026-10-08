class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def find_first():
            left = 0
            right = len(nums) - 1
            idx = -1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    idx = mid

            return idx

        def find_last():
            left = 0
            right = len(nums) - 1
            idx = -1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    idx = mid

            return idx

        return [find_first(), find_last()]
