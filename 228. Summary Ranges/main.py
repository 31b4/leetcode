class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = [] 
        for i, n in enumerate(nums):
            if ans and ans[-1][1] == n-1:
                ans[-1][1] = n
            else:
                ans.append([n, n])
        return [f'{x}->{y}' if x != y else f'{x}' for x, y in ans]
