class Solution:

    def isValid(self, s: str) -> bool:
        stack = []

        mapper = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in mapper:
                if not stack or stack.pop() != mapper[char]:
                    return False
            else:
                stack.append(char)
        return not stack
