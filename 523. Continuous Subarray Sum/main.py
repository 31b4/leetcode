class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for start in range(n - 1):  # Step 1: Iterate Through Starting Points
            for end in range(start + 1, n):  # Step 2: Expand the Subarray
                subarray_sum = sum(nums[start:end + 1])  # Step 3: Calculate the Sum
                if subarray_sum == 0 and k == 0:  # Handling special case where k is 0
                    return True
                if k != 0 and subarray_sum % k == 0:  # Step 4: Check if the Sum is a Multiple of k
                    return True
        return False  # Step 5: Return the Result
