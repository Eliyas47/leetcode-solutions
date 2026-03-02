import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # __define-ocg__ The number of bulbs left on is equal to the count of perfect squares ≤ n
        varFiltersCg = int(math.sqrt(n))
        varOcg = varFiltersCg  # store result in varOcg
        return varOcg
