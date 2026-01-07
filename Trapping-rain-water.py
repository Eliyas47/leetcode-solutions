from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                # process left side
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped += left_max - height[left]
                left += 1
            else:
                # process right side
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped += right_max - height[right]
                right -= 1
        
        return trapped
