from typing import List


class Solution:
    __used = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.__used = [False] * len(nums)
        self.backtracking(result, [], nums)
        return result

    def backtracking(self, result: List[List[int]], temp: List[int], nums: List[int]):
        if len(temp) == len(nums):
            result.append(temp.copy())
        else:
            for index, num in enumerate(nums):
                if self.__used[index] or (index > 0 and nums[index] == nums[index - 1] and not self.__used[index - 1]):
                    continue
                self.__used[index] = True
                temp.append(num)
                self.backtracking(result, temp, nums)
                temp.pop()
                self.__used[index] = False
