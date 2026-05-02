class Solution:
    def rotatedDigits(self, n: int) -> int:
        good_digits = {'2','5','6','9'}
        valid_digits = {'0','1','8'} | good_digits
        
        def is_good(num):
            s = str(num)
            return all(ch in valid_digits for ch in s) and any(ch in good_digits for ch in s)
        
        return sum(is_good(i) for i in range(1, n+1))
