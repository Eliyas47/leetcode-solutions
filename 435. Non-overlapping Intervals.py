class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        prev_end = float('-inf')
        
        for start, end in intervals:
            if start < prev_end:
                # Overlap → remove this interval
                count += 1
            else:
                # Keep interval → update end
                prev_end = end
        
        return count
