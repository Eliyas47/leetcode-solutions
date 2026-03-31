from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        num, den = 0, 1  # running fraction
        i = 0
        while i < len(expression):
            # parse sign
            sign = 1
            if expression[i] in "+-":
                if expression[i] == "-":
                    sign = -1
                i += 1
            
            # parse numerator
            j = i
            while expression[j] != "/":
                j += 1
            numerator = int(expression[i:j]) * sign
            
            # parse denominator
            i = j + 1
            j = i
            while j < len(expression) and expression[j] not in "+-":
                j += 1
            denominator = int(expression[i:j])
            i = j
            
            # update running fraction
            num = num * denominator + numerator * den
            den *= denominator
            
            # simplify
            g = gcd(abs(num), den)
            num //= g
            den //= g
        
        return f"{num}/{den}"
