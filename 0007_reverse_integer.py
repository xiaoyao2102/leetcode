class Solution:

    def reverse(self, x: int) -> int:

        int_max = 214748364
        int_min = -214748364

        rev = 0

        is_positive = x > 0

        while x != 0:

            quotient, reminder = divmod(x, 10)

            pop = reminder if is_positive or reminder == 0 else reminder - 10
            x = quotient if is_positive or reminder == 0 else quotient + 1

            if rev > int_max or (rev == int_max and pop > 7):
                return 0

            if rev < int_min or (rev == int_min and pop < -8):
                return 0

            rev = rev * 10 + pop

        return rev