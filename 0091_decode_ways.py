class Solution:

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            first = int(s[i - 1:i])
            second = int(s[i - 2:i])

            if 1 <= first <= 9:
                dp[i] += dp[i - 1]

            if 10 <= second <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]




solution = Solution()

# assert solution.numDecodings('12') == 2
# assert solution.numDecodings('226') == 3
# assert solution.numDecodings('2262') == 3
# assert solution.numDecodings('0') == 0
# assert solution.numDecodings('10') == 1
# assert solution.numDecodings('01') == 0
# assert solution.numDecodings('101') == 1
# assert solution.numDecodings('012') == 0
assert solution.numDecodings('100') == 0
assert solution.numDecodings('110') == 1
assert solution.numDecodings('12120') == 3

