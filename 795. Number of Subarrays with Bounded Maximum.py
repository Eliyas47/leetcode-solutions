from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound: int) -> int:
            res = cur = 0
            for num in nums:
                if num <= bound:
                    cur += 1
                    res += cur
                else:
                    cur = 0
            return res
        
        return count(right) - count(left - 1)
