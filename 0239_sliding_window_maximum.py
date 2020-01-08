from typing import List

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        result = []
        # find max number in the very first window.
        # save the maximum and the index of maximum
        max_num = max(nums[:k])
        max_idx = nums.index(max_num)

        # iterate numbers in given array, excluding the last (k - 1) numbers.
        # because the size of window cannot be over the array.
        # e.g. [1, 3, -1, -3, 5, 3, 6, 7] and k = 3
        # the final index in the iteration is 5 which comes from 8 - 3
        for i in range(len(nums) - k + 1):
            if i <= max_idx and nums[i + k - 1] < max_num:
                # this case indicates that
                # all number in the window which start from i with k size is not bigger than the current max number.
                # so just append the current max number to the result.
                result.append(max_num)
            elif i <= max_idx:
                # this case indicates that
                # the newest number is larger than current max number
                # so the max_num and max_idx should be replaced to the new one
                max_num = nums[i + k - 1]
                max_idx = i + k - 1
                result.append(max_num)
            else:
                # this case indicates that
                # the current index is larger than the index of max number,
                # which means the current max number is no longer in the window.
                # so we should find another max number from i to i + k.
                max_num = max(nums[i: i + k])
                max_idx = i + nums[i: i + k].index(max_num)
                result.append(max_num)

        return result


solution = Solution()
assert solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], k=3) == [3, 3, 5, 5, 6, 7]
assert solution.maxSlidingWindow([1], k=1) == [1]
assert solution.maxSlidingWindow([1, -1], k=1) == [1, -1]
assert solution.maxSlidingWindow([1, -9, 8, -6, 6, 4, 0, 5], k=4) == [8, 8, 8, 6, 6]
