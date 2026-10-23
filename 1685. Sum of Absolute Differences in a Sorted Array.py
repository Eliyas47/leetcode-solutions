
from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        prefix = 0
        result = []

        for i, x in enumerate(nums):
            right = total - x

            left_sum = x * i - prefix
            right_sum = right - x * (n - i - 1)

            result.append(left_sum + right_sum)

            prefix += x
            total -= x

        return result
