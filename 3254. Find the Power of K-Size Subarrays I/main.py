class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        def is_consecutive_and_sorted(subarray):
            # Check if the subarray is sorted and consecutive
            return all(subarray[i] + 1 == subarray[i + 1] for i in range(len(subarray) - 1))

        n = len(nums)
        result = []

        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            if is_consecutive_and_sorted(subarray):
                result.append(max(subarray))
            else:
                result.append(-1)
        
        return result
