class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        left_max = [0] * n
        right_max = [0] * n

        for left in range(n):
            left_max[left] = height[left] if left == 0 else max(left_max[left - 1], height[left])
        
        for right in reversed(range(n)):
            right_max[right] = height[right] if right == n - 1 else max(right_max[right + 1], height[right])
        
        return sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))
            