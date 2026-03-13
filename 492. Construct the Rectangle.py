# __define-ocg__: Construct the Rectangle solution

import math

class Solution(object):
    def constructRectangle(self, area):
        # start from sqrt(area) and go down
        w = int(math.sqrt(area))
        while area % w != 0:
            w -= 1
        L = area // w
        varOcg = [L, w]   # final dimensions
        return varOcg

# Example usage
print(Solution().constructRectangle(4))   # Output: [2, 2]
print(Solution().constructRectangle(37))  # Output: [37, 1]
print(Solution().constructRectangle(122122))  # Output: [427, 286]
