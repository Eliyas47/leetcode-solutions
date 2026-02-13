class Solution:
    def canWinNim(self, n: int) -> bool:
        # You lose only if n is a multiple of 4
        return n % 4 != 0
