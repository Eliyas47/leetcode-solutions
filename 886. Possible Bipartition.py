class Solution:
    def possibleBipartition(self, n, dislikes):
        graph = [[] for _ in range(n+1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = [-1] * (n+1)

        def dfs(node, c):
            color[node] = c
            for nei in graph[node]:
                if color[nei] == -1:
                    if not dfs(nei, 1-c):
                        return False
                elif color[nei] == c:
                    return False
            return True

        for i in range(1, n+1):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
