class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        
        hMax = vMax = 0
        hCount = vCount = 0

        for i in range(len(hBars)):
            if i != 0 and hBars[i] - hBars[i-1] != 1:
                hMax = max(hMax, hCount+1)
                hCount = 0
            hCount += 1
        hMax = max(hMax, hCount+1)

        for i in range(len(vBars)):
            if i != 0 and vBars[i] - vBars[i-1] != 1:
                vMax = max(vMax, vCount+1)
                vCount = 0
            vCount += 1
        vMax = max(vMax, vCount+1)

        return min(hMax, vMax) ** 2
