class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7
        ans = 0
        minstack = [(-inf, -1, 0)]
        for i, x in enumerate(arr):
            while minstack[-1][0] >= x:
                minstack.pop()
            sz = i - minstack[-1][1]
            minstack.append((arr[i], i, arr[i]*sz+minstack[-1][2]))
            ans += minstack[-1][2]
            ans %= MOD
        return ans
