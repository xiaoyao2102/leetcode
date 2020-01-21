from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        block = [[[] for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                char = board[i][j]

                if char == '.':
                    continue

                if char in row[i] or char in col[j] or char in block[i // 3][j // 3]:
                    return False
                row[i].append(char)
                col[j].append(char)
                block[i // 3][j // 3].append(char)

        return True


solution = Solution()

assert solution.isValidSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
])

assert not solution.isValidSudoku([
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
])

a = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

block_board = [[] for _ in range(9)]

for i in range(9):
    for j in range(9):
        block_board[i // 3 + (j // 3 * 3)].append(a[i][j])

from typing import Set
result = [[None for _ in range(9)] for _ in range(9)]

all_possible_num = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

# easy to get one col
reversed_board = list(zip(*a))

block_board = [[] for _ in range(9)]

for i in range(9):
    for j in range(9):
        block_board[i // 3 + (j // 3 * 3)].append(a[i][j])

print(block_board)

for i in range(9):
    for j in range(9):
        if a[i][j] == '.':
            possible = all_possible_num.difference(set(a[i])).difference(set(reversed_board[j])).difference(set(block_board[i // 3 + (j // 3 * 3)]))
            result[i][j] = possible

print(result)