class Solution:
    # T = O(Nlog(K)) for the heap popping happening n times 
    # S = O(K) for the heap
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ans = -math.inf, math.inf # max range to start with

        heap = []
        
        high = -math.inf
        # track max out of first starting list of numbers 
        # and also add them to min heap
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            high = max(high, nums[i][0])

        # Logic: At each iteration we have max element in list
        # and heap pop gives us min element in list and we go left to 
        # right.
        # Between these min and max we will cover at least one element in the array as we 
        # got the min and max out of taking one element from each array 
        # Now to reduce this window 
        # 1. we can reduce max -> but this will lead to an array from which this max 
        # came getting skipped 
        # 2. so we can only try to increase min as this can give us new window to consider
        # So we use min heap to get min out of current window and replace it with 
        # next element in the array that gave min
        # This will give use a new set of values to consider 
        # We will also track if this next element is greater than current max and update max
        # This way at each level we have 
        # 1. 1 element from each array 
        # 2. min from them and max from them 
        # and as we go from left to right we consider ranges with smaller start first 
        # as this is what we want (eg: 11 over 33) in [[1,2,3], [1,2,3], [1,2,3]]
        # This also is complete as we are not missing any range. Each time we only increment 
        # the smalest of all the numbers. Which means we are consiering the widest possible 
        # allowed range that has an element from each array and trying to reducing it.
        while True:
            low, id, ind = heapq.heappop(heap)

            # if new range is smaller then update ans
            if high - low < ans[1] - ans[0]:
                ans = (low, high)

            # if we reached the end of an array then we need to stop
            # as going further we will miss elements from this array
            if ind + 1 == len(nums[id]):
                return ans

            next = nums[id][ind+1]

            # find new max
            high = max(high, next)

            heapq.heappush(heap, (next, id, ind+1))
