from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = defaultdict(int)
        
        for row in wall:
            position = 0
            # exclude last brick to avoid rightmost edge
            for brick in row[:-1]:
                position += brick
                edge_count[position] += 1
        
        # max edges aligned
        max_edges = max(edge_count.values(), default=0)
        
        return len(wall) - max_edges
