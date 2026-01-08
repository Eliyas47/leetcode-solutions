from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # Result can be up to m + n digits
        result = [0] * (m + n)
        
        # Multiply each digit starting from the back
        for i in range(m - 1, -1, -1):
            digit1 = ord(num1[i]) - ord('0')
            for j in range(n - 1, -1, -1):
                digit2 = ord(num2[j]) - ord('0')
                
                # Multiply and add to existing result position
                product = digit1 * digit2
                pos1 = i + j
                pos2 = i + j + 1
                
                total = product + result[pos2]
                result[pos2] = total % 10
                result[pos1] += total // 10
        
        # Convert result array to string, skip leading zeros
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        
        # Join digits into string
        return ''.join(map(str, result[start:])) if start < len(result) else "0"
