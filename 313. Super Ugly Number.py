import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        seen = {1}
        heap = [1]

        for _ in range(n):
            val = heapq.heappop(heap)
            ugly_num = val
            for p in primes:
                nxt = val * p
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return ugly_num
