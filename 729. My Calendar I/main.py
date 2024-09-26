class MyCalendar:

    def __init__(self):
        # Initialize an empty list to store the events
        self.events = []
        
    def book(self, start: int, end: int) -> bool:
        # Check for overlap with existing events
        for s, e in self.events:
            # If the new event overlaps with any existing event
            if not (end <= s or start >= e):  # No overlap condition: (new_end <= old_start) or (new_start >= old_end)
                return False
        # If no overlap, add the event
        self.events.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
