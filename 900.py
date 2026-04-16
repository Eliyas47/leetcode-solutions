class RLEIterator:
    def __init__(self, encoding):
        # encoding is [count1, value1, count2, value2, ...]
        self.encoding = encoding
        self.index = 0  # pointer to current count
        self.remaining = encoding[0] if encoding else 0

    def next(self, n: int) -> int:
        while self.index < len(self.encoding) and n > 0:
            if self.remaining >= n:
                self.remaining -= n
                return self.encoding[self.index + 1]
            else:
                n -= self.remaining
                self.index += 2
                if self.index < len(self.encoding):
                    self.remaining = self.encoding[self.index]
        return -1
