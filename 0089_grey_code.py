from typing import List

"""


00 0 0
00 0 1
00 1 1
00 1 0
01 1 0
01 1 1
01 0 1
01 0 0
10 0 0
10 0 1
10 1 1
10 1 0
11 1 0
11 1 1
11 0 1
11 0 0


"""


class Solution:

    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        def get_bit(n: int) -> List[str]:
            if n == 1:
                return ['0', '1']
            else:
                last = get_bit(n - 1)

                return list(map(lambda x: '0' + x, last)) + list(map(lambda x: '1' + x, last[::-1]))

        return list(map(lambda x: int(x, 2), get_bit(n)))


solution = Solution()

assert solution.grayCode(3) == [0, 1, 3, 2, 6, 7, 5, 4]
