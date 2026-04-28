import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_heap = [(-freq, char) for char, freq in counts.items()]
        heapq.heapify(max_heap)
        
        prev = (0, "")
        result = []
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            
            if prev[0] < 0:
                heapq.heappush(max_heap, prev)
            
            prev = (freq + 1, char)  # decrease count
        
        res = "".join(result)
        return res if len(res) == len(s) else ""
