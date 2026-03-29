from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_map = defaultdict(int)
        count_map[0] = 1   # base case: sum starts at 0
        prefix_sum = 0
        result = 0
        
        for num in nums:
            prefix_sum += num
            # check if prefix_sum - k exists
            if (prefix_sum - k) in count_map:
                result += count_map[prefix_sum - k]
            # record prefix_sum
            count_map[prefix_sum] += 1
        
        return result
