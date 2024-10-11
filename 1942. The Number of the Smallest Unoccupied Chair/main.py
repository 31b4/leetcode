class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        order = sorted(range(len(times)), key = lambda x: times[x][0])  # <-- 1)
        emptySeats, takenSeats = list(range(len(times))), []            # <-- 2)

        for i in order:                                                 # <-- 3)
            ar, lv = times[i]

            while takenSeats and takenSeats[0][0] <= ar:
                heappush(emptySeats, heappop(takenSeats)[1])
            seat = heappop(emptySeats)                                  # <-- 4)

            if i == targetFriend: return seat

            heappush(takenSeats,(lv, seat))                             # <-- 5)
