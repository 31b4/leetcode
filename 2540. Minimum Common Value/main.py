class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2= len(nums1), len(nums2)
        if n1>n2:  return self.getCommon(nums2, nums1)
        prev=0
        for x in nums1:
            j=bisect_left(nums2, x, lo=prev)
            if j==n2: return -1
            elif x==nums2[j]: return x
            else: prev=j
        return -1
        
