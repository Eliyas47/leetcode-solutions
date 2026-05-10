class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        delta = (sumA - sumB) // 2
        bobSet = set(bobSizes)
        
        for x in aliceSizes:
            if x - delta in bobSet:
                return [x, x - delta]
