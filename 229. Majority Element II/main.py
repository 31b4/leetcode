class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        dct = {}
        n = len(nums)
        for x in set(nums):
            dct[x] = nums.count(x)
        for k, x in dct.items():
            if x > n//3:
                ans.append(k)
        return ans
