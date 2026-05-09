class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[m][k] = maximum number of floors that can be tested
        # with m moves and k eggs
        # We only need to track dp for current m
        dp = [0] * (k + 1)
        moves = 0

        # Keep increasing moves until we can cover n floors
        while dp[k] < n:
            moves += 1
            # Update dp backwards to avoid overwriting values we still need
            for eggs in range(k, 0, -1):
                dp[eggs] = dp[eggs] + dp[eggs - 1] + 1
        return moves
