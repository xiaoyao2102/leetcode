class Solution:

    def longestPalindrome(self, s: str) -> str:
        def palindrome(ss: str, l: int, r: int):
            while l >= 0 and r < len(ss) and ss[l] == ss[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        res = ''
        for i in range(len(s)):
            res = max(palindrome(s, i, i), palindrome(s, i, i + 1), res, key=len)
        return res
