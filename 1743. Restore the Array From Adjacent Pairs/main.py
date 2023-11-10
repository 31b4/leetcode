class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        
        startNode = 0
        res = []
        for a, b in adjacentPairs:
            adj[a].append(b)
            adj[b].append(a)
        for a in adj:
            if len(adj[a]) == 1:
                startNode = a
                break
            
        def dfs(node, prev):
            res.append(node)
            for nei in adj[node]:
                if nei != prev: dfs(nei, node)
        dfs(startNode, None)
        return res
