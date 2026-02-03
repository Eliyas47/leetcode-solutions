class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split both versions into lists of integers
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        # Find the maximum length
        n = max(len(v1), len(v2))
        
        # Pad shorter list with zeros
        while len(v1) < n:
            v1.append(0)
        while len(v2) < n:
            v2.append(0)
        
        # Compare revisions one by one
        for i in range(n):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        
        return 0
