class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        i = 1

        # Step 1: Find the first violation where digits[i-1] > digits[i]
        while i < len(digits) and digits[i-1] <= digits[i]:
            i += 1

        # If no violation, the number is already monotone increasing
        if i == len(digits):
            return n

        # Step 2: Backtrack to fix violation
        while i > 0 and digits[i-1] > digits[i]:
            digits[i-1] = str(int(digits[i-1]) - 1)
            i -= 1

        # Step 3: Set all digits after i to '9'
        for j in range(i+1, len(digits)):
            digits[j] = '9'

        # Step 4: Convert back to integer
        return int("".join(digits))
