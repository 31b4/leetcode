class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n=len(nums)
        x=0
        f=[0]*n

        for idx,val in enumerate(nums):
            if idx>=k:
                x^=f[idx-k]
            if x!=val:
                continue
            if k>n-idx:
                return -1
            x^=1
            f[idx]=1
        
        return sum(f)
