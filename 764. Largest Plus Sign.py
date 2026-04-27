from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # Step 1: Initialize grid with 1’s
        grid = [[1] * n for _ in range(n)]
        for r, c in mines:
            grid[r][c] = 0

        # Step 2: DP matrix to store min arm length at each cell
        dp = [[0] * n for _ in range(n)]

        # Step 3: Four directional passes
        for r in range(n):
            count = 0
            # Left to right
            for c in range(n):
                count = count + 1 if grid[r][c] == 1 else 0
                dp[r][c] = count
            count = 0
            # Right to left
            for c in range(n - 1, -1, -1):
                count = count + 1 if grid[r][c] == 1 else 0
                dp[r][c] = min(dp[r][c], count)

        for c in range(n):
            count = 0
            # Top to bottom
            for r in range(n):
                count = count + 1 if grid[r][c] == 1 else 0
                dp[r][c] = min(dp[r][c], count)
            count = 0
            # Bottom to top
            for r in range(n - 1, -1, -1):
                count = count + 1 if grid[r][c] == 1 else 0
                dp[r][c] = min(dp[r][c], count)

        # Step 4: Find maximum plus sign order
        ans = 0
        for r in range(n):
            for c in range(n):
                ans = max(ans, dp[r][c])

        return ans
