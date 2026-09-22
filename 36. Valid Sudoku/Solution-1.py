class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen_cells = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (
                    board[i][j] + "@row" + str(i) in seen_cells
                    or board[i][j] + "@column" + str(j) in seen_cells
                    or board[i][j] + "@box" + str(i // 3) + str(j // 3) in seen_cells
                ):
                    return False
                seen_cells.add(board[i][j] + "@row" + str(i))
                seen_cells.add(board[i][j] + "@column" + str(j))
                seen_cells.add(board[i][j] + "@box" + str(i // 3) + str(j // 3))

        return True
