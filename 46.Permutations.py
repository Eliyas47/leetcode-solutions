from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def backtrack():
            # If current length equals nums length, we formed a full permutation
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for num in nums:
                if num in current:
                    continue
                current.append(num)
                backtrack()
                # Backtrack: remove last added
                current.pop()

        backtrack()
        return result
