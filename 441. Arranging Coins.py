import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Using quadratic formula to solve k(k+1)/2 <= n
        return int((math.sqrt(8 * n + 1) - 1) // 2)
