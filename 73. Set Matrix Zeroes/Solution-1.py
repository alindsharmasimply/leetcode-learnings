class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        should_fill_first_row = 0 in matrix[0]
        should_fill_first_col = False
        for i in range(r):
            if matrix[i][0] == 0:
                should_fill_first_col = True
                break

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, r):
            for j in range(1, c):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if should_fill_first_row:
            matrix[0] = [0] * c

        if should_fill_first_col:
            for i in range(r):
                matrix[i][0] = 0
