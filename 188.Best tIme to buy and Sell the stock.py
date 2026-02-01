class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        # Special case: unlimited transactions
        if k >= n // 2:
            return sum(max(0, prices[i+1] - prices[i]) for i in range(n-1))
        
        # DP table: dimensions [n][k+1][2]
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]
        
        # Initialization
        for j in range(k+1):
            dp[0][j][1] = -prices[0]  # buying on day 0
        
        # Fill DP
        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        
        return dp[n-1][k][0]
