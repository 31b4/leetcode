class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        queue = deque(piles)
        res = 0
        while queue:
            queue.pop() # alice
            res += queue.pop() # us
            queue.popleft() # bob

        return res
