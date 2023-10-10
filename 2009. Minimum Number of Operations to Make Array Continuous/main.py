class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        uniq = list(set(nums))
        uniq.sort()
        ans,j = n,0
        n2 = len(uniq)
        for i in range(0,n2):
            while(j < n2 and uniq[j] < uniq[i] + n):
                j += 1
            ans = min(ans, n-j+i)
        return ans
