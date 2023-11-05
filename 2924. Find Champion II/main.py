class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        winner = set()
        for i in range(n):
            winner.add(i)
            
        for ed in edges:
            winner.discard(ed[1])
            
        if len(winner)>1:
            return -1
        
        for i in winner:
            return i
        
