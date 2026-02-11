import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Step 1: Create events (start and end of buildings)
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))  # building enters
            events.append((right, 0, 0))           # building exits

        # Step 2: Sort events by x-coordinate
        events.sort()

        # Step 3: Use a max heap to track active buildings
        result = []
        heap = [(0, float("inf"))]  # (height, end)
        prev_height = 0

        for x, neg_h, r in events:
            # Remove buildings that ended
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            # Add new building
            if neg_h != 0:
                heapq.heappush(heap, (neg_h, r))

            # Current max height
            curr_height = -heap[0][0]
            if curr_height != prev_height:
                result.append([x, curr_height])
                prev_height = curr_height

        return result
