from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            result.append(path[:])  # save current subset
            for i in range(start, len(nums)):
                path.append(nums[i])       # choose
                backtrack(i + 1, path)     # explore
                path.pop()                 # undo choice

        backtrack(0, [])
        return result
