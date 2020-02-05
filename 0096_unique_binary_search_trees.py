class Solution:

    def numTrees(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]


solution = Solution()

assert solution.numTrees(1) == 1
assert solution.numTrees(2) == 2
assert solution.numTrees(3) == 2 * 2 + 1 * 1
assert solution.numTrees(4) == 5 * 2 + 2 * 2
assert solution.numTrees(5) == 14 * 2 + 5 * 2 + 1 * 2 * 2
assert solution.numTrees(6) == 42 * 2 + 14 * 2 + 2 * 5 * 2

