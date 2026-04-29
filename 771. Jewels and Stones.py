class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)   # unique jewel types
        count = 0
        for s in stones:
            if s in jewel_set:
                count += 1
        return count
