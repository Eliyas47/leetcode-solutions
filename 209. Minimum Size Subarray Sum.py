from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_len = float('inf')

        # Expand the window with right pointer
        for right in range(len(nums)):
            total += nums[right]

            # Shrink the window while the sum is large enough
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        # If no subarray found, return 0
        return 0 if min_len == float('inf') else min_len
