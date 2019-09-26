from typing import List

class Solution:
    @staticmethod
    def extreme_insertion_index(nums: List[int], target: int, left: bool) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                high = mid
            else:
                low = mid + 1

        return low

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = Solution.extreme_insertion_index(nums, target, True)

        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]

        return [left_index, Solution.extreme_insertion_index(nums, target, False) - 1]
