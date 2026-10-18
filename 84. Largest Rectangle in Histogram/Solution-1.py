class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                j, popped_height = stack.pop()
                start = j
                width = i - j
                area = popped_height * width
                max_area = max(max_area, area)
            stack.append((start, height))

        while stack:
            j, popped_height = stack.pop()
            width = n - j
            area = popped_height * width
            max_area = max(max_area, area)

        return max_area
