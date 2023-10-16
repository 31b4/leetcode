class Solution:
    def getRow(self, n: int) -> List[int]:
        ans = [1]
        for k in range(1, n + 1):
            ans.append(ans[k-1] * (n - k + 1) // k)
        return ans
