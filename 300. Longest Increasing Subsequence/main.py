class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [nums.pop(0)]
        for n in nums:
            if n > arr[-1]:
                arr.append(n)
            else:
                arr[bisect_left(arr, n)] = n
        return len(arr)
