class Solution:
    def findReplaceString(self, s, indices, sources, targets):
        # Pair up indices with sources and targets
        replacements = sorted(zip(indices, sources, targets))
        
        result = []
        i = 0
        while i < len(s):
            replaced = False
            for idx, src, tgt in replacements:
                if i == idx and s[i:i+len(src)] == src:
                    result.append(tgt)
                    i += len(src)
                    replaced = True
                    break
            if not replaced:
                result.append(s[i])
                i += 1
        return "".join(result)
