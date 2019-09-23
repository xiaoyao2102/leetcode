class Solution:

    def fourSum(self, nums: list, target: int) -> list:

        def n_sum(left: int, right: int, reduced_target: int, n: int, result: list, results: list):
            # termination condition
            if right - left + 1 < n or n < 2 or nums[left] * n > reduced_target or nums[right] * n < target:
                return
            elif n == 2:
                while left < right:
                    s = nums[left] + nums[right]

                    if s == reduced_target:
                        results.append(result + [nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

                    elif s < reduced_target:
                        left += 1
                    elif s > reduced_target:
                        right -= 1
            else:
                for i in range(left, right + 1):
                    if i == left or (i > left and nums[i - 1] != nums[i]):
                        n_sum(i + 1, right, reduced_target - nums[i], n - 1, result + [nums[i]], results)

        nums.sort()
        results = []
        n_sum(0, len(nums) - 1, target, 4, [], results)
        return results
