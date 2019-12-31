from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_can_reach = 0

        for index, num in enumerate(nums):
            if index > max_can_reach:
                return False
            max_can_reach = max(max_can_reach, index + num)
        return True
