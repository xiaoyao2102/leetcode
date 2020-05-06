from typing import List


class Solution:
    _used = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self._used = [False] * len(nums)
        self.backtracking(result, [], nums)
        return result

    def backtracking(self, result: List[List[int]], temp: List[int], nums: List[int]):
        if len(temp) == len(nums):
            result.append(temp.copy())
        else:
            for index, num in enumerate(nums):
                if self._used[index] or (index > 0 and nums[index] == nums[index - 1] and not self._used[index - 1]):
                    continue
                self._used[index] = True
                temp.append(num)
                self.backtracking(result, temp, nums)
                temp.pop()
                self._used[index] = False
