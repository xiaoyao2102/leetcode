class Solution:

    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 0

        self.count = 0

        self._dfs(0, 0, 0, 0, n)

        return self.count

    # col left_below and right_below are integers that represent the position whether is
    # attacked by other queens.
    # e.g. left below = 5 = 0101 means that the first and third position is available
    def _dfs(self, row_number: int, col: int, left_below: int, right_below: int, n: int):
        if row_number >= n:
            self.count += 1
            return

        # get available bit
        # col | left_below | right_below can find which bit is 0 for current position
        # ~ change the 0 to 1 for easier to get.
        # (1 << n) - 1 is a bit mask that contains n 1.
        # e.g. 00...0011...11   num of 1 = n
        bit = (~ (col | left_below | right_below)) & ((1 << n) - 1)

        while bit > 0:
            # get last bit of 1
            p = bit & -bit

            # enter next row recursion
            # col | p. put p in col
            # (left_down | p) << 1.
            # put p in left_down. because in the next row, the p will attack the left
            # down position, thus we need to move p 1 position to the left.
            # so as right_down

            self._dfs(row_number + 1, col | p, (left_below | p) << 1, (right_below | p) >> 1, n)

            # remove last bit of 1
            bit = bit & (bit - 1)


solution = Solution()
assert solution.totalNQueens(4) == 2
