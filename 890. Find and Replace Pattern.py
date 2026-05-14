class Solution:
    def findAndReplacePattern(self, words, pattern):
        def normalize(word):
            mapping = {}
            normalized = []
            next_id = 0
            for ch in word:
                if ch not in mapping:
                    mapping[ch] = next_id
                    next_id += 1
                normalized.append(mapping[ch])
            return normalized
        
        pattern_norm = normalize(pattern)
        return [w for w in words if normalize(w) == pattern_norm]
