from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        self.backtrack(result, [], candidates, target, 0)
        return result

    def backtrack(self, result: List[List[int]], temp_list: List[int], candidates, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            result.append(temp_list.copy())
        else:
            i = start
            while i < len(candidates) and remain >= candidates[i]:
                if i > start and candidates[i] == candidates[i - 1]:
                    i += 1
                    continue
                temp_list.append(candidates[i])
                self.backtrack(result, temp_list, candidates, remain - candidates[i], i + 1)
                temp_list.pop()
                i += 1
