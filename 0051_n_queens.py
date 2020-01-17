from copy import deepcopy
from typing import List


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        temp_board = [['.' for j in range(n)] for i in range(n)]
        self.__backtrack(res, temp_board, 0, n)
        return list(map(lambda board: list(map(lambda x: ''.join(x), board)), res))

    def __backtrack(self, res, temp_board, row, n):
        if row == n:
            res.append(deepcopy(temp_board))
            return

        for col in range(n):
            if self.__is_valid(temp_board, row, col, n):
                temp_board[row][col] = 'Q'
                self.__backtrack(res, temp_board, row + 1, n)
                temp_board[row][col] = '.'

    def __is_valid(self, temp_board, row, col, n):
        if self.__check_column(temp_board, row, col):
            return False

        if self.__check_upper_45(temp_board, row, col):
            return False

        if self.__check_upper_135(temp_board, row, col, n):
            return False

        return True

    def __check_column(self, temp_board, row, col):
        i = 0
        while i != row:
            if temp_board[i][col] == 'Q':
                return True
            i += 1
        return False

    def __check_upper_45(self, temp_board, row, col):
        i, j = row - 1, col - 1

        while i >= 0 and j >= 0:
            if temp_board[i][j] == 'Q':
                return True
            i -= 1
            j -= 1
        return False

    def __check_upper_135(self, temp_board, row, col, n):
        i, j = row - 1, col + 1

        while i >= 0 and j < n:
            if temp_board[i][j] == 'Q':
                return True
            i -= 1
            j += 1
        return False
