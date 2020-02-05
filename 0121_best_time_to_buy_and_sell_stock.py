from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        dp = [[0, 0] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = - prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][1], - prices[i])

        return dp[-1][0]


solution = Solution()

assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert solution.maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2
assert solution.maxProfit([1, 2]) == 1
