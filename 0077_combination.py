from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n or not k:
            return []

        result = []

        def back_track(temp_list: List[int], current: int):
            if len(temp_list) == k:
                result.append(temp_list.copy())
                return

            for i in range(current, n + 1):
                temp_list.append(i)
                back_track(temp_list, i + 1)
                temp_list.pop()

        back_track([], 1)

        return result


solution = Solution()

assert solution.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
assert solution.combine(1, 1) == [[1]]
assert solution.combine(3, 1) == [[1], [2], [3]]
