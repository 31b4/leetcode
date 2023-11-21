class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] - int(str(nums[i])[::-1])

        res = 0
        dic = collections.defaultdict(int)
        for num in nums:
            res = (res+dic[num]) % 1000000007
            dic[num] += 1
        
        return res
