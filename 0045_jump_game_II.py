class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        str_pointer, pattern_pointer = 0, 0
        asterisk_pattern_start = -1
        match = 0
        while str_pointer < len(s):

            if pattern_pointer < len(p) and (p[pattern_pointer] == '?' or p[pattern_pointer] == s[str_pointer]):
                str_pointer += 1
                pattern_pointer += 1
            elif pattern_pointer < len(p) and p[pattern_pointer] == '*':
                asterisk_pattern_start = pattern_pointer
                match = str_pointer
                pattern_pointer += 1
            elif asterisk_pattern_start != -1:
                pattern_pointer = asterisk_pattern_start + 1
                match += 1
                str_pointer = match
            else:
                return False

        while pattern_pointer < len(p) and p[pattern_pointer] == '*':
            pattern_pointer += 1
        return pattern_pointer == len(p)