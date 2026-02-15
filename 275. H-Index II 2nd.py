class Solution:
    def hIndex(self, citations):
        n = len(citations)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Papers with at least citations[mid] = n - mid
            if citations[mid] == n - mid:
                return citations[mid]
            elif citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid - 1
        
        return n - left
