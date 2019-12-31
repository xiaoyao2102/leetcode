from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            word_set = tuple(sorted(word))
            if word_set in result:
                result[word_set].append(word)
            else:
                result[word_set] = [word]
        return result.values()
