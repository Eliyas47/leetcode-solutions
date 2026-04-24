from typing import List
from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Step 1: Extract letters from licensePlate
        required = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        
        # Step 2: Check each word
        result = None
        for word in words:
            word_count = Counter(word)
            if all(word_count[ch] >= required[ch] for ch in required):
                if result is None or len(word) < len(result):
                    result = word
        return result
