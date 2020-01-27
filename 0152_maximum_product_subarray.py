from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        positive_max = nums.copy()
        negative_max = nums.copy()

        for i in range(1, len(nums)):
            positive_max[i] = positive_max[i - 1] * nums[i] if nums[i] >= 0 else negative_max[i - 1] * nums[i]
            positive_max[i] = max(positive_max[i], nums[i])
            negative_max[i] = negative_max[i - 1] * nums[i] if nums[i] >= 0 else positive_max[i - 1] * nums[i]
            negative_max[i] = min(negative_max[i], nums[i])

        return max(positive_max)


solution = Solution()

assert solution.maxProduct([2, 3, -2, 4]) == 6
assert solution.maxProduct([-2, 0, -1]) == 0
assert solution.maxProduct([2, 3, -10, 5, -1]) == 300
assert solution.maxProduct([0, 2]) == 2
assert solution.maxProduct([2, -5, -2, -4, 3]) == 24
