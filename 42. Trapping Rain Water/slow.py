# working solutions, just not fast enough 
# main.py is faster, using two pointers

class Solution:
    def trap(self, H: List[int]) -> int:#lefele valo optimalizalas kell
        maxH = max(H)
        minH = min(H)
        ans = 0
        level = maxH
        Y = 0
        seen = []
        while level >= minH+1:
            i = 0
            while i < len(H):
                x = H[i]
                r = 1
                if i in seen:
                    i+=1
                    continue
                if x < level and i != 0 and i != len(H):
                    LEFT = False
                    RIGHT = False
                    sv = 0

                    for j in range(i + 1, len(H)):
                        sv += 1
                        if H[j] >= level:
                            RIGHT = True
                            r = j-1
                            break
                            
                    for j in range(i - 1, -1, -1):
                        if H[j] >= level:
                            LEFT = True
                            break
                    if RIGHT and LEFT:
                        r=1
                        below = level - x-1
                        for j in range(below):
                            seen.append(i)
                        i += sv - 1
                        if below > 0:
                            sv += below
                            i += 1
                        ans += sv
                    elif not RIGHT:
                        level -= 1
                        i = 0
                Y += 1
                i += r
            level -= 1
        return ans  
                    
