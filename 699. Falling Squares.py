class Solution:
    def fallingSquares(self, positions):
        ans = []
        intervals = []  # store [left, right, height]
        max_height = 0
        
        for left, size in positions:
            right = left + size
            height = size
            for l, r, h in intervals:
                if not (r <= left or right <= l):  # overlap
                    height = max(height, h + size)
            intervals.append([left, right, height])
            max_height = max(max_height, height)
            ans.append(max_height)
        
        return ans
