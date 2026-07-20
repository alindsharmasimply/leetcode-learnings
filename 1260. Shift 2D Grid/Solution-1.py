from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)  # number of rows
        n = len(grid[0])  # number of columns

        # If k is a multiple of total elements, the grid remains unchanged
        k %= m * n

        ans = [[0] * n for _ in range(m)]

        for row in range(m):
            for column in range(n):

                # flattening of the 2D array
                old_1D = (row * n) + column

                # after the shift
                new_1D = (old_1D + k) % (
                    m * n
                )  # not to exceed the total number of elements

                # unflatten the 1D array
                new_row = new_1D // n
                new_column = new_1D % n

                ans[new_row][new_column] = grid[row][column]

        return ans
