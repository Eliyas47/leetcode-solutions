class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        k = 1024

        dp = [[0] * k for _ in range(n)]

        for i in range(m):
            for j in range(n):
                curr = [False] * k

                if i == 0 and j == 0:
                    curr[grid[i][j]] = True
                else:
                    prev = dp[j] if i > 0 else None
                    left = dp[j - 1] if j > 0 else None

                    for x in range(k):
                        if prev and prev[x]:
                            curr[x ^ grid[i][j]] = True
                        if left and left[x]:
                            curr[x ^ grid[i][j]] = True

                dp[j] = curr

        return next(x for x in range(k) if dp[n - 1][x])
