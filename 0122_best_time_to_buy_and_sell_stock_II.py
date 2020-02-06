from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


solution = Solution()

assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7
assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
