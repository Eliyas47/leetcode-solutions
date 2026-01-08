from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # If n <= 1, we're already at the end
        if n <= 1:
            return 0
        
        jumps = 0
        curr_end = 0
        curr_farthest = 0
        
        for i in range(n - 1):
            # Update the farthest we can reach from current range
            curr_farthest = max(curr_farthest, i + nums[i])
            
            # When we reach the end of the current jump range
            if i == curr_end:
                jumps += 1
                curr_end = curr_farthest
        
        return jumps
