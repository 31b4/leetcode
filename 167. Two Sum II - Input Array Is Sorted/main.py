class Solution:
    def twoSum(self, N: List[int], target: int) -> List[int]:
        i = 0
        j = len(N) - 1
        ans = []
        while i < j:
            summ = N[i] + N[j]
            if summ == target:
                return [i+1, j+1]
            elif summ > target:
                j -= 1
            else:
                i += 1
        return ans 
