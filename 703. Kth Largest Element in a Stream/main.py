class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)  # Convert nums into a heap
        # If the heap is larger than k, remove the smallest elements until it has exactly k elements
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        heapq.heappush(self.nums, val)
        # If after adding the new value, the heap has more than k elements, pop the smallest
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # The smallest element in the heap is now the k-th largest element
        return self.nums[0]
