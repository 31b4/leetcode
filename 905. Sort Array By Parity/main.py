class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        parity = []
        nonParity = []
        for x in nums:
            if x % 2 == 0:
                parity.append(x)
            else:
                nonParity.append(x)
        return parity + nonParity
