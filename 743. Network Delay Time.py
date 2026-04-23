import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build adjacency list
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Step 2: Min-heap for Dijkstra
        heap = [(0, k)]  # (time, node)
        dist = {}
        
        # Step 3: Process nodes
        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = time
            for nei, w in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + w, nei))
        
        # Step 4: Check if all nodes are reached
        if len(dist) != n:
            return -1
        return max(dist.values())
