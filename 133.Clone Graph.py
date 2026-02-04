# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        visited = {}
        
        def dfs(n):
            if n in visited:
                return visited[n]
            
            # Clone the node
            clone = Node(n.val)
            visited[n] = clone
            
            # Clone neighbors recursively
            for nei in n.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return clone
        
        return dfs(node)
