class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = 0
        stack = [(1, 0, 0)]

        while stack:
            node, parent, d = stack.pop()
            depth = max(depth, d)

            for neighbor in graph[node]:
                if neighbor != parent:
                    stack.append((neighbor, node, d + 1))

        return pow(2, depth - 1, 10**9 + 7)
