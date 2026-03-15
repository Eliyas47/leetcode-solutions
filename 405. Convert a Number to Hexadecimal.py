# __define-ocg__: Convert a Number to Hexadecimal solution

class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"
        
        # Handle negative numbers with 32-bit mask
        if num < 0:
            num += 2 ** 32
        
        hex_chars = "0123456789abcdef"
        result = []
        
        while num > 0:
            result.append(hex_chars[num % 16])
            num //= 16
        
        varOcg = "".join(reversed(result))
        return varOcg

# Example usage
print(Solution().toHex(26))   # Output: "1a"
print(Solution().toHex(-1))   # Output: "ffffffff"
