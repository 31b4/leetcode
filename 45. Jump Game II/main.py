class Solution:
    def jump(self, nums: List[int]) -> int:
        for i,x in enumerate(nums[1:]):
            nums[i+1] = max(nums[i+1] + i+1, nums[i])
        dist = 0
        ans = 0
        while dist < len(nums)-1:
            ans += 1
            dist = nums[dist]
        return ans
