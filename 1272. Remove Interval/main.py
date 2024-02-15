class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        r1,r2 = toBeRemoved
        res = []
        for x,y in intervals:
            if r1 <= x and r2 >= y:
                continue

            if r1 > x and r2 < y:
                res.append([x,r1])
                res.append([r2,y])
            elif r1 < y and r1 > x:
                res.append([x,r1])
            elif r2 >= x and r2 < y:
                res.append([r2,y])
            
            else:
                res.append([x,y])    
        return res            


