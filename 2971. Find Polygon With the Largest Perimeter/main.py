class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 0
        sv_res = sum(nums[:2])

        for x in nums[2:]:
            if sv_res > x:
                res = sv_res + x
            sv_res += x

        return -1 if not res else res
