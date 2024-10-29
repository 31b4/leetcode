class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        min1, min2 = [0, -1], [0, -1] # (cost, color) pair
        for i in range(len(costs)):
            cur_min1, cur_min2 = [float('inf'), 0], [float('inf'), 0]
            for j in range(len(costs[0])):
                cost = min1[0] + costs[i][j]
                # conflict
                if j == min1[1]: 
                    cost =  min2[0] + costs[i][j]
                # update cur_min cost
                if cost <= cur_min1[0]:
                    cur_min2[0], cur_min2[1] = cur_min1[0], cur_min1[1]
                    cur_min1[0], cur_min1[1] = cost, j
                elif cost < cur_min2[0]:
                    cur_min2[0], cur_min2[1] = cost, j
            min1, min2 = cur_min1, cur_min2            
        return min1[0]
