class Solution:
    def makeGood(self, s: str) -> str:
        
        ss = []
        
        for c in s: 
            if ss and ss[-1] == c.swapcase():    # if the stack is not empty and the last letter on the stack is
                ss.pop()                         # a match for the current letter (e.g., 'a' and 'A'), remove both
            else: 
                ss.append(c)                     # continue adding to stack to compare with next letter
        
        return "".join(ss)
