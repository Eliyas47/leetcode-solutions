class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # frequency buckets, index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        # iterate from highest possible frequency to lowest
        for freq in range(len(buckets) - 1, -1, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
