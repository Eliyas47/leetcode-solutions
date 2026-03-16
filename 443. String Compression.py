class Solution:
    def compress(self, chars) -> int:
        write = 0  # position to write compressed characters
        read = 0   # position to read characters
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count consecutive characters
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if > 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        
        return write
