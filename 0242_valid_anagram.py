from collections import Counter


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


solution = Solution()
assert solution.isAnagram('anagram', 'nagaram')
assert not solution.isAnagram('rat', 'car')
assert not solution.isAnagram('aa', 'a')
assert not solution.isAnagram('ccca', 'aacc')
