class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        nums = [x - y for x, y in zip(nums1, nums2)]
        nums.sort()
        
        print(nums)
        n = len(nums)
        res = 0
        for i, x in enumerate(nums):
            if x > 0:
                res += n - i - 1
                continue

            l, r = i + 1, n - 1
            while l <= r:
                m = (l + r) >> 1
                if x + nums[m] > 0:
                    r = m - 1
                else:
                    l = m + 1
            res += n - l

        return res
