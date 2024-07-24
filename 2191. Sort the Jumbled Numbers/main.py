class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(x):
            if x==0: return mapping[0]
            z=0
            pow10=1
            while x>0:
                q, r=divmod(x, 10)
                z+=mapping[r]*pow10
                x=q
                pow10*=10
            return z
        n=len(nums)
        mapNum=[]
        for i, x in enumerate(nums):
            mapNum.append([convert(x), i, x])
        mapNum.sort()
        for i in range(n):
            nums[i]=mapNum[i][2]
        return nums
        
        
