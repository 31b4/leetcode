class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        maps = {}
        for start, end in paths:
            maps[start] = end
        ans = paths[0][0]
        while True:
            try:
                ans = maps[ans]
            except:
                return ans
