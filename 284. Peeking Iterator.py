# Let's assume the Iterator class is already defined with:
# next() and hasNext() methods.

class PeekingIterator:
    def __init__(self, iterator):
        # Store the original iterator
        self.iterator = iterator
        # Cache the next element if available
        self._next = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        # Return the cached element without advancing
        return self._next

    def next(self):
        # Return the cached element and advance the iterator
        current = self._next
        self._next = self.iterator.next() if self.iterator.hasNext() else None
        return current

    def hasNext(self):
        # True if cached element exists
        return self._next is not None
