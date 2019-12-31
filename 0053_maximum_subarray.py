from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        max_val, sum_val = nums[0], nums[0]

        for i in range(1, len(nums)):
            if sum_val < 0:
                sum_val = nums[i]
            else:
                sum_val += nums[i]
            max_val = max(max_val, sum_val)
        return max_val
