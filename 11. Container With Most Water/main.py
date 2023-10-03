class Solution:
    def maxArea(self, H: List[int]) -> int:
        ans = 0
        left = 0
        right = len(H)-1
        while left < right:
            area = (right-left) * min(H[left],H[right])
            ans = max(area,ans)
            if H[left] > H[right]:
                right -= 1
            else:
                left += 1 
        return ans
