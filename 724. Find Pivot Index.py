class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # right sum = total - left_sum - num
            if left_sum == total - left_sum - num:
                return i
            left_sum += num
        
        return -1
