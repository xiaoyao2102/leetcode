class Solution:

    def myPow(self, x, n):
        if not n:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        return x * self.myPow(x, n - 1) if n % 2 else self.myPow(x * x, n // 2)
