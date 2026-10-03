from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        dq = deque()
        left = right = 0
        results = []

        while right < n:
            # 1. Remove smaller elements
            while dq and nums[right] >= nums[dq[-1]]:
                dq.pop()

            # 2. Append current index
            dq.append(right)

            # 3. Remove out-of-bounds indices
            if dq[0] < left:
                dq.popleft()

            # 4. Add to results once the first window is ready
            if right + 1 >= k:
                results.append(nums[dq[0]])
                left += 1

            right += 1

        return results
