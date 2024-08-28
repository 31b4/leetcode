class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        r, c= len(grid1), len(grid1[0])
        N=r*c
        root=[i for i in range(N+1)]
        Size=[1]*(N+1)
        merge=0

        def Find(x):
            if x==root[x]: return x
            root[x]=Find(root[x])
            return root[x]
        
        def Union(x, y):
            nonlocal merge
            x, y=Find(x), Find(y)
            if x==y: return False
            if Size[x]>Size[y]:
                Size[x]+=Size[y]
                root[y]=x
            else:
                Size[y]+=Size[x]
                root[x]=y
            merge+=1
            return True
        def idx(i, j): return i*c+j

        cntLand=0
        for i, row in enumerate(grid2):
            for j, cell in enumerate(row):
                curr, down, right= idx(i, j), idx(i+1,j), idx(i, j+1)
                g2=cell==1
                cntLand+=g2
                if g2:
                    if i+1<r and grid2[i+1][j]:
                        Union(curr, down) 

                    if j+1<c and grid2[i][j+1]:
                        Union(curr, right)

                    if grid1[i][j]==0:
                        Union(curr, N) #connecting to water-cell N no sub-Island
        return cntLand-merge
                    
        
            
        
