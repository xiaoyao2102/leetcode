from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lis = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
                continue

            j = 0
            while nums[i] > lis[j]:
                j += 1
            lis[j] = nums[i]

        return len(lis)


solution = Solution()

assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert solution.lengthOfLIS([1, 2, 3, 4]) == 4
assert solution.lengthOfLIS([5, 3, 2]) == 1
