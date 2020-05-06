class Solution:

    def generateParenthesis(self, n: int) -> list:
        ans = []

        def back_tracking(p: str, left: int, right: int):
            if len(p) == 2 * n:
                ans.append(p)
                return

            if left < n:
                back_tracking(p + '(', left + 1, right)

            if right < left:
                back_tracking(p + ')', left, right + 1)

        back_tracking('', 0, 0)
        return ans
