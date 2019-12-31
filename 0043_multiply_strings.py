class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                product = self.to_int(num1[i]) * self.to_int(num2[j])
                p1, p2 = i + j, i + j + 1
                total = product + res[p2]

                res[p1] += total // 10
                res[p2] = total % 10
        return ''.join(map(lambda x: str(x), res)).lstrip('0')

    def to_int(self, digit_str: str) -> int:
        return ord(digit_str) - ord('0')
