class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        
        def overlap(x_shift, y_shift):
            count = 0
            for i in range(n):
                for j in range(n):
                    if 0 <= i + x_shift < n and 0 <= j + y_shift < n:
                        if img1[i][j] == 1 and img2[i + x_shift][j + y_shift] == 1:
                            count += 1
            return count
        
        max_overlap = 0
        for x in range(-n+1, n):
            for y in range(-n+1, n):
                max_overlap = max(max_overlap, overlap(x, y))
        return max_overlap
