class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set()
        duplicate = -1
        for num in nums:
            if num in num_set:
                duplicate = num
            num_set.add(num)
        
        missing = (n * (n + 1)) // 2 - (sum(nums) - duplicate)
        return [duplicate, missing]
