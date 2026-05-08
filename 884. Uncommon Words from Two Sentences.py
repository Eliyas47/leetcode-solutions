from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split both sentences into words
        words = s1.split() + s2.split()
        
        # Count frequencies
        freq = Counter(words)
        
        # Collect words that appear exactly once
        return [word for word, count in freq.items() if count == 1]
