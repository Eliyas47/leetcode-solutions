from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mapping = defaultdict(list)
        for a, b, c in allowed:
            mapping[(a, b)].append(c)
        
        memo = {}
        
        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True
            if row in memo:
                return memo[row]
            
            def build_next(i, path):
                if i == len(row) - 1:
                    return dfs(path)
                if (row[i], row[i+1]) not in mapping:
                    return False
                for ch in mapping[(row[i], row[i+1])]:
                    if build_next(i+1, path+ch):
                        return True
                return False
            
            memo[row] = build_next(0, "")
            return memo[row]
        
        return dfs(bottom)
