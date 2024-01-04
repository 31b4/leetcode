class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        if cnt.most_common()[-1][1] == 1 : return -1
        return sum((c-1) // 3 + 1 for c in cnt.values())
