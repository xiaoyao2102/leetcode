class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = ''
        while i >= 0 or j >= 0 or carry:
            current_sum = carry
            current_sum += self.__to_int(a[i]) if i >= 0 else 0
            current_sum += self.__to_int(b[j]) if j >= 0 else 0

            res += str(current_sum % 2)
            carry = current_sum // 2

            i -= 1
            j -= 1

        return res[::-1]

    def __to_int(self, num):
        return ord(num) - ord('0')
