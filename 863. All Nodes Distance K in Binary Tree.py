from collections import deque

class Solution:
    def distanceK(self, root, target, k):
        # Step 1: Build a map of parents for each node
        parent_map = {}
        def find_parents(node, par=None):
            if node:
                parent_map[node] = par
                find_parents(node.left, node)
                find_parents(node.right, node)
        
        find_parents(root)
        
        # Step 2: BFS starting from the target node
        queue = deque([(target, 0)]) # (node, current_distance)
        visited = {target}
        
        while queue:
            # If the nodes at the front of the queue are at distance k,
            # all remaining nodes in the queue at this level are the answer.
            if queue[0][1] == k:
                return [node.val for node, dist in queue]
            
            node, dist = queue.popleft()
            
            # Check all 3 possible directions (Left, Right, Parent)
            for neighbor in [node.left, node.right, parent_map[node]]:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
                    
        return []
