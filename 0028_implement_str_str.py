class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        target_len = len(needle)
        for i in range(len(haystack) - target_len + 1):
            if haystack[i: i + target_len] == needle:
                return i
        return -1