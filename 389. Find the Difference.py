class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        freq_s, freq_t = Counter(s), Counter(t)
        for ch in freq_t:
            if freq_t[ch] != freq_s.get(ch, 0):
                return ch
