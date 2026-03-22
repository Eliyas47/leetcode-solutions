class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # number of unique candy types
        unique_types = len(set(candyType))
        # maximum Alice can eat
        max_allowed = len(candyType) // 2
        return min(unique_types, max_allowed)
