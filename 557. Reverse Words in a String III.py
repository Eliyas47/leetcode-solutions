class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words
        words = s.split(" ")
        
        # Reverse each word
        reversed_words = [word[::-1] for word in words]
        
        # Join them back with spaces
        return " ".join(reversed_words)
