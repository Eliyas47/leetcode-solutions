
from typing import List

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        stones = sorted(
            zip(aliceValues, bobValues),
            key=lambda x: x[0] + x[1],
            reverse=True
        )

        alice = sum(stones[i][0] for i in range(0, len(stones), 2))
        bob = sum(stones[i][1] for i in range(1, len(stones), 2))

        return (alice > bob) - (alice < bob)
