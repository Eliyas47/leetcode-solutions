class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp[i][j] = length of longest palindromic subsequence in s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the table for substrings of increasing length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][n - 1]
