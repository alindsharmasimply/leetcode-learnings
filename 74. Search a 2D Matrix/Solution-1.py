class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n

        while left < right:
            mid = (left + right) // 2

            row = mid // n
            column = mid % n

            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                left = mid + 1
            else:
                right = mid

        return False
