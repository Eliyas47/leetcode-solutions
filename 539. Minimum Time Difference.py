class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert times to minutes
        minutes = []
        for t in timePoints:
            h, m = map(int, t.split(":"))
            minutes.append(h * 60 + m)
        
        # Sort times
        minutes.sort()
        
        # Initialize min_diff with large value
        min_diff = float("inf")
        
        # Compare adjacent times
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
        
        # Wrap-around difference (last vs first across midnight)
        wrap_diff = 1440 + minutes[0] - minutes[-1]
        min_diff = min(min_diff, wrap_diff)
        
        return min_diff
