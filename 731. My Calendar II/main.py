class MyCalendarTwo:
    def __init__(self):
        # List to hold the booked intervals
        self.bookings = []
        
    def book(self, start: int, end: int) -> bool:
        # Check for overlaps with existing bookings
        for a, b in self.bookings:
            # Check if the new booking overlaps with the existing interval
            if start < b and end > a:
                # Calculate the overlapping sub-interval
                new_start = max(a, start)
                new_end = min(b, end)
                
                # Check if the sub-interval overlaps more than once
                if self.check(new_start, new_end):
                    return False  # Overlapping more than once, booking fails
        
        # If there are no conflicts, add the booking
        self.bookings.append((start, end))
        return True  # Booking successful
    
    def check(self, start: int, end: int) -> bool:
        overlap_count = 0
        
        for a, b in self.bookings:
            # Check for strict overlap
            if start < b and end > a:
                overlap_count += 1
                if overlap_count == 2:
                    return True  # Found more than one overlap
        
        return False  # No overlapping found
