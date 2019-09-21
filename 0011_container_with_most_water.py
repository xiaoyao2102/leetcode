class Solution:

    def maxArea(self, height: list) -> int:
        max_area, l, r = 0, 0, len(height) - 1

        while l < r:
            l_height = height[l]
            r_height = height[r]

            max_area = max(max_area, l_height * (r - l) if l_height < r_height else r_height * (r - l))

            if l_height < r_height:
                l += 1
            elif l_height > r_height:
                r -= 1
            else:
                l += 1
                r -= 1

        return max_area
