class Solution:
    def findNthDigit(self, n: int) -> int:
        length, count, start = 1, 9, 1
        
        # Step 1: Find the digit length group
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        
        # Step 2: Find the target number
        num = start + (n - 1) // length
        
        # Step 3: Extract the digit
        digit_index = (n - 1) % length
        return int(str(num)[digit_index])
