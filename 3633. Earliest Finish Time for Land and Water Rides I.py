class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        def calc(s1, d1, s2, d2):
            earliest = min(s + d for s, d in zip(s1, d1))
            return min(max(earliest, s) + d for s, d in zip(s2, d2))

        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration)
        )
