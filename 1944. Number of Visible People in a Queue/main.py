class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans, stack = [0] * len(heights), deque()
        for i, H in enumerate(heights[::-1]):
            while stack and stack[-1] < H:
                ans[i]+= 1
                stack.pop()
            if stack: ans[i] += 1
            stack.append(H)
        return ans[::-1]
