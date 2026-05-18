from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = []

        def dfs(node: int):
            path.append(node)
            if node == len(graph) - 1:
                res.append(path[:])  # copy current path
            else:
                for nei in graph[node]:
                    dfs(nei)
            path.pop()  # backtrack

        dfs(0)
        return res
