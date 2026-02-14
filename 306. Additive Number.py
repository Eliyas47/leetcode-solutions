class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        # Try all possible splits for first and second numbers
        for i in range(1, n):
            for j in range(i+1, n):
                # First number
                a, b = num[:i], num[i:j]

                # Skip if numbers have leading zeros
                if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
                    continue

                a, b = int(a), int(b)
                k = j

                # Build sequence
                while k < n:
                    c = a + b
                    c_str = str(c)

                    # If next part of num doesn't match c, break
                    if not num.startswith(c_str, k):
                        break

                    # Advance
                    k += len(c_str)
                    a, b = b, c

                # If we consumed the whole string, it's valid
                if k == n:
                    return True

        return False
