class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if not height:
            return 0

        left = 0
        right = n - 1

        max_left = height[left]
        max_right = height[right]

        ans = 0

        while left < right:
            if max_left < max_right:
                ans += max_left - height[left]
                left += 1
                max_left = max(max_left, height[left])
            
            else:
                ans += max_right - height[right]
                right -= 1
                max_right = max(max_right, height[right])
        
        return ans