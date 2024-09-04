class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dir=['N','E','S','W']
        d=0
        x=0
        y=0
        res=0
        s=set((i,j) for i,j in obstacles)
        for i in range(len(commands)):
            if commands[i]==-1:
                d+=1
                d=d%4
            elif  commands[i]==-2:
                d-=1
                d=d%4
            else:
                if dir[d]=='N':
                    for move in range(commands[i]):
                        if (x,y+1) in s:
                            break
                        y+=1
                elif dir[d]=='E':
                    for move in range(commands[i]):
                        if (x+1,y) in s:
                            break
                        x+=1
                elif dir[d]=='S':
                    for move in range(commands[i]):
                        if (x,y-1) in s:
                            break
                        y-=1
                else:
                    for move in range(commands[i]):
                        if (x-1,y) in s:
                            break
                        x-=1
            res=max(res,x**2+y**2)
        return res



        
