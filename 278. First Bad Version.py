# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                right = mid          # possible bad version → search left half
            else:
                left = mid + 1       # good version → search right half
        
        return left
