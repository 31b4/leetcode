class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        duplicated = 1
        n = len(name) - 1
        m = len(typed)
        typed_idx = 0
        for i,c in enumerate(name):
            print(c)
            if i < n and name[i+1] == c:
                duplicated +=1
            elif i < n and name[i+1] != c:
                if typed_idx + duplicated >= m:
                    return False
                for _ in range(duplicated):
                    if typed[typed_idx] != c:
                        return False
                    typed_idx += 1
                while typed_idx < m and typed[typed_idx] == c:
                    typed_idx+=1
                duplicated = 1
            elif i == n:
                if typed_idx >= m:
                    return False
                for x in typed[typed_idx:]:
                    if x!= c:
                        return False

        return True
            

            
