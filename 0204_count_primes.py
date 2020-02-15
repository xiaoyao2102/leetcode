class Solution:

    def countPrimes(self, n: int) -> int:
        count = [1] * n

        for i in range(2, int(n ** 0.5) + 1):
            if count[i]:
                count[i * i:n:i] = [0] * ((n - 1 - i ** 2) // i + 1)

        return max(0, sum(count) - 2)


solution = Solution()

assert solution.countPrimes(102) == 26
