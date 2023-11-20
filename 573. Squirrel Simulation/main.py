class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        # Nut which is farthest from tree but closest to squirrel,
        # is the for which dx is high but sx is low.
        # Or the one for which dx - sx is maximum.
        starter_nut = []
        sv = float("-inf")

        for nut in nuts:
            min_to_nut = abs(nut[0]-squirrel[0]) + abs(nut[1]-squirrel[1]) 
            max_to_tree = abs(nut[0]-tree[0]) + abs(nut[1]-tree[1])
            if max_to_tree - min_to_nut > sv:
                sv = max_to_tree - min_to_nut
                starter_nut = nut
        
        #to starter_nut to tree distance
        res = (
            abs(squirrel[0]-starter_nut[0]) + abs(squirrel[1]-starter_nut[1]) +
            abs(tree[0]-starter_nut[0]) + abs(tree[1]-starter_nut[1])
        )

        # add up every other nut
        for nut in nuts:
            if nut == starter_nut:# already visited
                continue
            res += (abs(nut[0]-tree[0]) + abs(nut[1]-tree[1])) *2
        
            
        return res
