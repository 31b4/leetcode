class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def arithmetic(arr):
            arr.sort()
            diff = arr[1] - arr[0]
            for i in range(len(arr)-1):
                if arr[i+1] -  arr[i] != diff:
                    return False
            return True
        
        res = []
        for i in range(len(l)):
            res.append(arithmetic(nums[l[i]:r[i]+1]))

        return res
