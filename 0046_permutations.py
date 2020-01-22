from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(result, [], nums)
        return result

    def backtracking(self, result: List[List[int]], used_num: List[int], nums: List[int]):
        if len(used_num) == len(nums):
            result.append(used_num.copy())
        else:
            for num in nums:
                if num in used_num:
                    continue
                used_num.append(num)
                self.backtracking(result, used_num, nums)
                used_num.pop()
