from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] True if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        # Patterns starting with '*' can match empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' matches empty (dp[i][j-1]) or one more char (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # '?' or exact char
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]
