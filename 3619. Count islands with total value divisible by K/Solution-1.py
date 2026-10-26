class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        count_divisible_by_k = 0

        def dfs_sum(r: int, c: int):
            total_sum = grid[r][c]
            grid[r][c] = 0  # marked as visited
            directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

            for i, j in directions:
                nr = r + i
                nc = c + j
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                    total_sum += dfs_sum(nr, nc)

            return total_sum

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    island_sum = dfs_sum(i, j)
                    if island_sum % k == 0:
                        count_divisible_by_k += 1

        return count_divisible_by_k
