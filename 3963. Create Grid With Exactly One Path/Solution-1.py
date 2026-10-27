class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        top_row = '.' * n

        other_row = '#' * (n - 1) + '.'

        return [top_row] + [other_row] * (m - 1)