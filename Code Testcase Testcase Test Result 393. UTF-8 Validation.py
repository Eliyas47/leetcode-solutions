class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # number of bytes remaining for current character
        remaining = 0

        for byte in data:
            # mask to get only last 8 bits
            byte = byte & 0xFF

            if remaining == 0:
                # Count leading ones
                if (byte >> 5) == 0b110:
                    remaining = 1
                elif (byte >> 4) == 0b1110:
                    remaining = 2
                elif (byte >> 3) == 0b11110:
                    remaining = 3
                elif (byte >> 7) == 0:
                    remaining = 0
                else:
                    return False
            else:
                # Must be a continuation byte: starts with 10
                if (byte >> 6) != 0b10:
                    return False
                remaining -= 1

        return remaining == 0
