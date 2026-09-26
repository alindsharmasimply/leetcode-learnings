class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top = 0
        bottom = len(matrix) - 1

        while top < bottom:
            for i in range(bottom - top):
                left = top
                right = bottom

                top_left = matrix[top][left + i]

                matrix[top][left + i] = matrix[bottom - i][left]

                matrix[bottom - i][left] = matrix[bottom][right - i]

                matrix[bottom][right - i] = matrix[top + i][right]

                matrix[top + i][right] = top_left

            top += 1
            bottom -= 1
