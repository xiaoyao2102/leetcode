from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [[[- float('Infinity') for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]

        dp[0][0][0] = 0
        dp[0][1][1] = - prices[0]

        for i in range(1, len(prices)):
            dp[i][0][0] = 0
            dp[i][0][1] = - float('Infinity')

            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])

            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i])
            dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i])

        return max(map(lambda x: x[0], dp[-1]))


solution = Solution()

assert solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
