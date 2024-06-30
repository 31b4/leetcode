class UnionFind:
    """A minimalist standalone union-find implementation."""
    def __init__(self, n):
        self.count = n               # number of disjoint sets 
        self.parent = list(range(n)) # parent of given nodes
        self.rank = [1]*n            # rank (aka size) of sub-tree 
        
    def find(self, p):
        """Find with path compression."""
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p]) # path compression 
        return self.parent[p]
    
    def union(self, p, q):
        """Union with ranking."""
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False
        self.count -= 1 # one more connection => one less disjoint 
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt # add small sub-tree to large sub-tree for balancing
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt] # ranking 
        return True
    
        
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa = UnionFind(n) # for Alice
        ufb = UnionFind(n) # for Bob
        
        ans = 0
        edges.sort(reverse=True) 
        for t, u, v in edges: 
            u, v = u-1, v-1
            if t == 3: ans += not (ufa.union(u, v) and ufb.union(u, v)) # Alice & Bob
            elif t == 2: ans += not ufb.union(u, v)                     # Bob only
            else: ans += not ufa.union(u, v)                            # Alice only
        return ans if ufa.count == 1 and ufb.count == 1 else -1 # check if uf is connected 
