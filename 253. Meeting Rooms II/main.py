class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        rooms = 0
        
        if not intervals:
            return 0
        
        endp = 0
        
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        
        for i in range(len(starts)):
            if starts[i]>=ends[endp]:
                endp+=1
            else:
                rooms+=1
        
        return rooms
