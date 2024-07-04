class DSU:
    def __init__(self,n):
        self.parents = list(range(n+1))
        self.ranks = [0]*(n+1)
        self.components = n 
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a , b):
        aParent = self.find(a)
        bParent = self.find(b)
        if aParent == bParent :
            return
        if self.ranks[aParent] > self.ranks[bParent]:
            self.parents[bParent] = aParent
        elif self.ranks[bParent] > self.ranks[aParent]:
            self.parents[aParent] = bParent
        else:
            self.parents[bParent] = aParent
            self.ranks[bParent] += 1

        self.components -= 1
    
    def isSingle(self):
        return self.components == 1
    

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x: x[0])
        lastTimeStamp = 0
        people = DSU(n)
        for log in logs:
            timestamp, u, v = log
            lastTimeStamp = timestamp
            if people.find(u) != people.find(v):
                people.union(u,v)
            if people.isSingle():
                break
        if people.isSingle():
            return lastTimeStamp
        return -1
