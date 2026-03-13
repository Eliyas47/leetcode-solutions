# __define-ocg__: Teemo Attacking solution

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        total = 0
        for i in range(len(timeSeries) - 1):
            total += min(duration, timeSeries[i+1] - timeSeries[i])
        total += duration
        varOcg = total
        return varOcg

# Example usage
print(Solution().findPoisonedDuration([1,4], 2))   # Output: 4
print(Solution().findPoisonedDuration([1,2], 2))   # Output: 3
