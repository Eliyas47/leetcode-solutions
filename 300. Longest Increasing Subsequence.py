class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n  # dp[i] = length of LIS ending at i

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
