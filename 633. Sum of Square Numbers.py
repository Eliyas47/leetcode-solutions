import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b = c - a * a
            if int(math.sqrt(b)) ** 2 == b:
                return True
            a += 1
        return False
