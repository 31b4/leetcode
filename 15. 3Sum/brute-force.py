class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        setn = set({})
        nums = sorted(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sv = [nums[i], nums[j], nums[k]]
                        setn.add(tuple(sv))
        return setn
