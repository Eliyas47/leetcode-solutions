class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            num = (left + right) // 2   # our current guess
            result = guess(num)         # call the guess API
            
            if result == 0:             # num is correct
                return num
            elif result == -1:          # num is higher
                right = num - 1
            else:                       # result == 1 → num is lower
                left = num + 1
