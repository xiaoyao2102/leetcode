from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        for i in range(len(s)):
            for w in wordDict:
                if w == s[i - len(w) + 1:i + 1] and (i - len(w) == -1 or dp[i - len(w)]):
                    dp[i] = True

        return dp[-1]


solution = Solution()
assert solution.wordBreak('leetcode', ['leet', 'code'])
assert solution.wordBreak('applepenapple', ['apple', 'pen'])
assert not solution.wordBreak('catsandog', ['cats', 'and', 'dog', 'sand', 'cat'])