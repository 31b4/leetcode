class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(x) for x in accounts)
