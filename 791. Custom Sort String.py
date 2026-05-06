class Solution:
    def customSortString(self, order: str, s: str) -> str:
        from collections import Counter
        
        # Count frequency of each character in s
        count = Counter(s)
        result = []
        
        # Place characters according to 'order'
        for ch in order:
            if ch in count:
                result.append(ch * count[ch])
                del count[ch]
        
        # Place remaining characters (not in 'order')
        for ch, freq in count.items():
            result.append(ch * freq)
        
        return "".join(result)
