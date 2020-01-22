from typing import List
from itertools import combinations


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums) + 1):
            res.extend(combinations(nums, i))
        return res


solution = Solution()

print(solution.subsets([1, 2, 3]))
