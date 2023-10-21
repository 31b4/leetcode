class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        maxSum = nums[0]
        MSL = deque()

        for i in range(len(nums)):
            nums[i] += MSL[0] if MSL else 0
            maxSum = max(maxSum, nums[i])
            while MSL and nums[i] > MSL[-1]:
                MSL.pop()
            if nums[i] > 0:
                MSL.append(nums[i])
            if i >= k and MSL and MSL[0] == nums[i - k]:
                MSL.popleft()

        return maxSum
