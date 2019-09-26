class Solution:

    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[len(nums) - 1]

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if abs(total - target) < abs(result - target):
                    result = total

                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    break
        return result
