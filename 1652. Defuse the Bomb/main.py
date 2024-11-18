class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        
        # If k == 0, all elements should be 0
        if k == 0:
            return [0] * n

        # Double the array to simulate circular behavior
        extended_code = code * 2

        # Handle positive and negative k
        if k > 0:
            return [sum(extended_code[i + 1:i + 1 + k]) for i in range(n)]
        else:
            k = abs(k)
            return [sum(extended_code[i + n - k:i + n]) for i in range(n)]
