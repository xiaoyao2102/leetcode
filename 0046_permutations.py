from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(result, [], nums)
        return result

    def backtracking(self, result: List[List[int]], temp: List[int], nums: List[int]):
        if len(temp) == len(nums):
            result.append(temp.copy())
        else:
            for num in nums:
                if num in temp:
                    continue
                temp.append(num)
                self.backtracking(result, temp, nums)
                temp.pop()
