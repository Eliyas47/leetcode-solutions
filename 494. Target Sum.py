# __define-ocg__: Target Sum solution

class Solution(object):
    def findTargetSumWays(self, nums, target):
        total = sum(nums)
        # If impossible, return 0
        if (target + total) % 2 != 0 or abs(target) > total:
            return 0
        subset_sum = (target + total) // 2
        
        # DP array
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        
        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]
        
        varOcg = dp[subset_sum]
        return varOcg

# Example usage
print(Solution().findTargetSumWays([1,1,1,1,1], 3))  # Output: 5
print(Solution().findTargetSumWays([1], 1))          # Output: 1
