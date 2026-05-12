class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]  # convert to binary string
        prev = -1
        max_gap = 0
        for i, bit in enumerate(binary):
            if bit == '1':
                if prev != -1:
                    max_gap = max(max_gap, i - prev)
                prev = i
        return max_gap
