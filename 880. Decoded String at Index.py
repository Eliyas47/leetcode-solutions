class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        # Forward pass: compute total length
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1
        
        # Backward pass: find k-th character
        for ch in reversed(s):
            if ch.isdigit():
                size //= int(ch)
                k %= size
                if k == 0:
                    k = size
            else:
                if k == size:
                    return ch
                size -= 1
