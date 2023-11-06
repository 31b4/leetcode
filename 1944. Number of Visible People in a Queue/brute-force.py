class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = []
        for i,x in enumerate(heights):
            if i == len(heights)-1:
                res.append(0)
                break
            cur_high = 0
            can_see = 0
            for j in range(i+1,len(heights)):
                if heights[j] < cur_high:
                    continue
                if heights[j] > x:
                    can_see+=1
                    break
                elif heights[j]>cur_high:
                    can_see += 1
                    cur_high = heights[j]
            res.append(can_see)
        return res
