class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal = defaultdict(list)
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonal[i+j] = [nums[i][j]] + diagonal[i+j]
        
        res = []
        for _, val in diagonal.items():
            res += val
        return res
