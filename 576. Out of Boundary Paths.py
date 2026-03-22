class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        result = 0
        
        for move in range(maxMove):
            new_dp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if dp[i][j] > 0:
                        for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                            ni, nj = i + x, j + y
                            if 0 <= ni < m and 0 <= nj < n:
                                new_dp[ni][nj] = (new_dp[ni][nj] + dp[i][j]) % MOD
                            else:
                                result = (result + dp[i][j]) % MOD
            dp = new_dp
        return result
