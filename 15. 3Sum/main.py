class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()
        ans = []
        n = len(nums)
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return s
