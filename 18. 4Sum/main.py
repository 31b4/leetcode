class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
      nums.sort()
      ll = set()
      for i in range(len(nums)):
          for j in range(i+1,len(nums)):
              l = j+1
              r = len(nums)-1
              while l<r:
                t = nums[i]+nums[j]+nums[l]+nums[r]
                if t == target:
                    ll.add((nums[i],nums[j],nums[l],nums[r]))
                if t<target:
                    l+=1
                else:
                    r-=1
      return ll
