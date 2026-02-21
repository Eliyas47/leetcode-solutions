class Solution:
    def maxCoins(self, nums):
        # Add 1 to both ends to simplify calculations
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[i][j] = max coins from bursting balloons between i and j (exclusive)
        dp = [[0] * n for _ in range(n)]
        
        # Interval DP
        for length in range(2, n):  # length of interval
            for left in range(0, n - length):
                right = left + length
                # Try bursting each balloon k last in (left, right)
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right]
                    )
        
        return dp[0][n - 1]
