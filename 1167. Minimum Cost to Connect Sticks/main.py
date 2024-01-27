class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        ans = 0
        while len(sticks) != 1:
            sticks.sort()
            sv = sticks[0] + sticks[1]
            sticks = sticks[2:] + [sv]
            ans += sv
        return ans
