class Solution:
    def expressiveWords(self, s, words):
        def RLE(word):
            groups = []
            i = 0
            while i < len(word):
                j = i
                while j < len(word) and word[j] == word[i]:
                    j += 1
                groups.append((word[i], j - i))
                i = j
            return groups
        
        s_groups = RLE(s)
        count = 0
        
        for w in words:
            w_groups = RLE(w)
            if len(s_groups) != len(w_groups):
                continue
            stretchy = True
            for (sc, sl), (wc, wl) in zip(s_groups, w_groups):
                if sc != wc:
                    stretchy = False
                    break
                if sl < 3 and sl != wl:
                    stretchy = False
                    break
                if sl >= 3 and wl > sl:
                    stretchy = False
                    break
            if stretchy:
                count += 1
        return count
