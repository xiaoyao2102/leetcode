class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []

        from collections import Counter, defaultdict

        word_bag = Counter(words)
        word_len, words_num = len(words[0]), len(words)
        total_len = words_num * word_len
        res = []

        for i in range(len(s) - total_len + 1):
            seen = defaultdict(int)
            for j in range(i, i + total_len, word_len):
                current_word = s[j: j + word_len]
                if current_word in word_bag:
                    seen[current_word] += 1
                    if seen[current_word] > word_bag[current_word]:
                        break
                else:
                    break
            if seen == word_bag:
                res.append(i)
        return res
