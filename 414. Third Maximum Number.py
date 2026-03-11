class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Use a set to remove duplicates
        distinct = list(set(nums))
        # Sort in descending order
        distinct.sort(reverse=True)
        
        # If there are at least 3 distinct numbers, return the third
        if len(distinct) >= 3:
            return distinct[2]
        # Otherwise, return the maximum
        return distinct[0]
