class Solution:
    def largestSumOfAverages(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        def avg(i, j):
            return (prefix[j] - prefix[i]) / (j - i)
        
        dp = [[0] * (k+1) for _ in range(n+1)]
        
        # Base case: one group
        for i in range(1, n+1):
            dp[i][1] = avg(0, i)
        
        # Fill DP table
        for j in range(2, k+1):
            for i in range(j, n+1):
                for p in range(j-1, i):
                    dp[i][j] = max(dp[i][j], dp[p][j-1] + avg(p, i))
        
        return dp[n][k]
