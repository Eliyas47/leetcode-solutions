from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(x: int) -> int:
            return sum(int(d) for d in str(x))
        
        return min(digit_sum(x) for x in nums)
