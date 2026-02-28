class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        # Break into as many 3's as possible
        quotient, remainder = divmod(n, 3)
        
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            # If remainder is 1, make one 3 into 4 (2+2)
            return 3 ** (quotient - 1) * 4
        else:  # remainder == 2
            return 3 ** quotient * 2
