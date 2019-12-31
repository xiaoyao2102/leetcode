from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = []
        start = n * n + 1

        while start > 1:
            start, end = start - len(res), start
            res = [tuple(range(start, end))] + list(zip(*res[::-1]))
        return res
