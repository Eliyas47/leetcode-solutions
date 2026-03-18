class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False  # 1 is not a perfect number
        
        total = 1  # 1 is always a divisor
        # Check divisors up to sqrt(num)
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                total += i
                if i != num // i:  # avoid double-counting square roots
                    total += num // i
        
        return total == num
