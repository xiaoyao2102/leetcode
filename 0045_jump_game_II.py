from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        current_end, current_farthest, jump = 0, 0, 0

        for i in range(len(nums) - 1):
            current_farthest = max(current_farthest, i + nums[i])
            if i == current_end:
                jump += 1
                current_end = current_farthest
        return jump
