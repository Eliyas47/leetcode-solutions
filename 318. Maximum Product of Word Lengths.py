class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Precompute bitmasks for all words
        masks = []
        lengths = []
        
        for w in words:
            bitmask = 0
            for c in w:
                bitmask |= 1 << (ord(c) - ord('a'))
            masks.append(bitmask)
            lengths.append(len(w))
        
        max_prod = 0
        
        # Compare every pair
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                # If no common letters
                if masks[i] & masks[j] == 0:
                    max_prod = max(max_prod, lengths[i] * lengths[j])
        
        return max_prod
