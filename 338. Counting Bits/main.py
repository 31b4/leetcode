class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        cnt = 0
        for x in range(n+1):
            cnt = bin(x).count("1")
            ans.append(cnt)
        return ans
