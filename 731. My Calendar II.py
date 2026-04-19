class MyCalendarTwo:

    def __init__(self):
        self.booked = []       # single bookings
        self.overlaps = []     # double bookings

    def book(self, start: int, end: int) -> bool:
        # Check against double bookings
        for s, e in self.overlaps:
            if start < e and end > s:  # overlap with double booking
                return False

        # Check against single bookings
        for s, e in self.booked:
            if start < e and end > s:  # overlap with single booking
                self.overlaps.append((max(start, s), min(end, e)))

        # Add to single bookings
        self.booked.append((start, end))
        return True
