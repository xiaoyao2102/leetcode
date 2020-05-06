from typing import List, Set


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        self._possible_nums = self._pre_process(board)

        self._solve(board)

    def _solve(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in self._possible_nums[i][j]:
                        if self._is_valid(board, i, j, num):
                            board[i][j] = num

                            if self._solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False

        return True

    def _is_valid(self, board, row, col, num):
        for i in range(9):
            if board[i][col] != '.' and board[i][col] == num:
                return False
            if board[row][i] != '.' and board[row][i] == num:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != '.' and board[3 * (row // 3) + i // 3][
                    3 * (col // 3) + i % 3] == num:
                return False
        return True

    def _pre_process(self, board: List[List[str]]) -> List[List[Set[str]]]:
        result = [[Set[str] for _ in range(9)] for _ in range(9)]

        all_possible_num = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        # easy to get one col
        reversed_board = list(zip(*board))

        block_board = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                block_board[i // 3 + (j // 3 * 3)].append(board[i][j])

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    possible = all_possible_num.difference(set(board[i])).difference(set(reversed_board[j])).difference(
                        set(block_board[i // 3 + (j // 3 * 3)]))
                    result[i][j] = possible

        return result

