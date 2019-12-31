from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        self.solve(board)

    def solve(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if self.is_valid(board, i, j, num):
                            board[i][j] = num

                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False

        return True

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[i][col] != '.' and board[i][col] == num:
                return False
            if board[row][i] != '.' and board[row][i] == num:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != '.' and board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True