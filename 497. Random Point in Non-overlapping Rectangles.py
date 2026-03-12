import random

# __define-ocg__: Random Point in Non-Overlapping Rectangles

class Solution(object):
    def __init__(self, rects):
        self.rects = rects
        self.varFiltersCg = []  # prefix sums of areas
        total = 0
        for x1, y1, x2, y2 in rects:
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            total += area
            self.varFiltersCg.append(total)
        self.total = total

    def pick(self):
        # choose rectangle based on weighted area
        target = random.randint(1, self.total)
        # binary search for rectangle index
        lo, hi = 0, len(self.varFiltersCg) -
