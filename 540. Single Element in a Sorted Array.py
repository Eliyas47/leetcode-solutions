class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                # Single element is on the right
                low = mid + 2
            else:
                # Single element is on the left (including mid)
                high = mid
        
        return nums[low]
