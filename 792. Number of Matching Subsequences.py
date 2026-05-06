from collections import defaultdict
import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # Preprocess: map each char to its indices in s
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)
        
        def is_subsequence(word: str) -> bool:
            prev = -1
            for ch in word:
                if ch not in pos:
                    return False
                # Find index > prev using binary search
                idx_list = pos[ch]
                j = bisect.bisect_right(idx_list, prev)
                if j == len(idx_list):
                    return False
                prev = idx_list[j]
            return True
        
        count = 0
        for w in words:
            if is_subsequence(w):
                count += 1
        return count
