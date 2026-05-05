class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        result = []
        
        for i, word in enumerate(words, 1):
            if word[0] in vowels:
                transformed = word + "ma"
            else:
                transformed = word[1:] + word[0] + "ma"
            transformed += "a" * i
            result.append(transformed)
        
        return " ".join(result)
