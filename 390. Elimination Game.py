class Solution:
    def lastRemaining(self, n: int) -> int:
        head, step, left = 1, 1, True
        remaining = n
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2
            left = not left
        return head
