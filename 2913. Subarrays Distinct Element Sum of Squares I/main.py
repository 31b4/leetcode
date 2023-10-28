class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            distinct_db = set()
            for j in range(i, n):
                distinct_db.add(nums[j])
                ans += len(distinct_db) * len(distinct_db)
        return ans
