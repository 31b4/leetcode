class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return ""
            
        stack = []
        stack.append(num[0])
        
        for i in range(1, len(num)):
            digit = num[i]
            
            while stack and stack[-1] > digit and k:
                stack.pop() # remove peak
                k -= 1
            
            stack.append(digit)
        
        while k:
            stack.pop() # now we just want to remove any additional elements from the end
            k -= 1
        
        res = "".join(stack).lstrip("0")
        
        return res if res != "" else "0"
