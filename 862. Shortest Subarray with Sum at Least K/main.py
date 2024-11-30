class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        heap = []
        curr_sum = 0
        res = float('inf')
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            if k <= curr_sum:
                res = min(res, i + 1)
           
            while heap and k <= curr_sum - heap[0][0]:
                res = min(res, i - heapq.heappop(heap)[1])

            heapq.heappush(heap, (curr_sum, i))

        return res if res != float('inf') else -1
