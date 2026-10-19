class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        ans = 0
        histogram = [0] * len(matrix[0])

        def largest_histogram_area(heights: list[int]):
            stack = []
            max_area = 0
            n = len(heights)

            for i, height in enumerate(heights):
                start = i
                while stack and height < stack[-1][1]:
                    j, popped_height = stack.pop()
                    start = j
                    width = i - j
                    max_area = max(max_area, popped_height * width)
                stack.append((start, height))

            while stack:
                j, popped_height = stack.pop()
                width = n - j
                max_area = max(max_area, popped_height * width)

            return max_area

        for row in matrix:
            for i, col in enumerate(row):
                histogram[i] = 0 if col == "0" else histogram[i] + 1
            ans = max(ans, largest_histogram_area(histogram))

        return ans
