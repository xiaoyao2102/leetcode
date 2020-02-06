from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        sell, buy, prev_sell = 0, - prices[0], 0

        for price in prices:
            sell, buy, prev_sell = max(buy + price, sell), max(prev_sell - price, buy), sell

        return sell


solution = Solution()

assert solution.maxProfit([1, 2, 3, 0, 2]) == 3
# assert solution.maxProfit([1, 2, 4]) == 3
