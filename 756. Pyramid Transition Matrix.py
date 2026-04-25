from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Build mapping
        mapping = defaultdict(list)
        for a, b, c in allowed:
            mapping[(a, b)].append(c)
        
        # Recursive function
        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True
            
            # Generate all possible next rows
            def build_next(i, path):
                if i == len(row) - 1:
                    return dfs(path)
                if (row[i], row[i+1]) not in mapping:
                    return False
                for ch in mapping[(row[i], row[i+1])]:
                    if build_next(i+1, path+ch):
                        return True
                return False
            
            return build_next(0, "")
        
        return dfs(bottom)
