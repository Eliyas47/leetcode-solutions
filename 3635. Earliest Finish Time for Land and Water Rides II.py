from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def calc(start1, duration1, start2, duration2):
            earliest = min(s + d for s, d in zip(start1, duration1))
            return min(
                max(earliest, s) + d
                for s, d in zip(start2, duration2)
            )

        return min(
            calc(landStartTime, landDuration,
                 waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration,
                 landStartTime, landDuration)
        )
