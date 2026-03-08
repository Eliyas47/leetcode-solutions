class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        S = sum(nums)
        
        # Compute F(0)
        F = sum(i * num for i, num in enumerate(nums))
        max_val = F
        
        # Use recurrence relation
        for k in range(1, n):
            F = F + S - n * nums[-k]
            max_val = max(max_val, F)
        
        return max_val
