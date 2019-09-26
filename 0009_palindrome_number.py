class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        half_num = 0

        while x > half_num:
            x, reminder = divmod(x, 10)
            half_num = half_num * 10 + reminder

        return half_num == x or x == (half_num // 10)
