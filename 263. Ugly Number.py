class Solution:
    def isUgly(self, n: int) -> bool:
        # Ugly numbers must be positive
        if n <= 0:
            return False

        # Keep dividing by 2, 3, and 5
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        # If we reduced it all the way to 1, it's ugly
        return n == 1
