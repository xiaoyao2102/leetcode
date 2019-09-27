from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        def add(element):
            if element in seen:
                return False
            seen.add(element)
            return True

        for i in range(10):
            for j in range(10):
                char = board[i][j]

                if char != '.':
                    if (not add(char + 'row' + str(i))) or (not add(char + 'column' + str(j))) or (not add(char + 'block' + str(i // 3) + str(j // 3))):
                        return False

        return True
