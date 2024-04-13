from collections import deque

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        ans = 0
        hist = [0] * len(matrix[0])
        
        for row in matrix:
            for i in range(len(row)):
                hist[i] = hist[i] + 1 if row[i] == '1' else 0
            ans = max(ans, self.largestRectangleArea(hist))
        
        return ans
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = deque()
        
        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        
        return ans
