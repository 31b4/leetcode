class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i, (start, end) in enumerate(intervals[:-1]):
            if end > intervals[i+1][0]:
                return False

        return True

