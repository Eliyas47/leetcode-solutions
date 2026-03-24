class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2
        
        # Step 1: Find pivot
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i < 0:
            return -1
        
        # Step 2: Find smallest digit greater than pivot
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        
        # Step 3: Swap
        digits[i], digits[j] = digits[j], digits[i]
        
        # Step 4: Reverse suffix
        digits[i + 1:] = reversed(digits[i + 1:])
        
        result = int("".join(digits))
        
        # Step 5: Check 32-bit range
        return result if result < 2**31 else -1
