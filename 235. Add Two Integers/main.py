class Solution:
    def sum(self, num1: int, num2: int) -> int:
        if num1==0 and num2==0: return 0
        if 0<num1: 
            return 1 + self.sum(num1-1,num2)
        if 0<num2:
             return 1 + self.sum(num1,num2-1)
        if num1<0:
             return -1 + self.sum(num1+1,num2)
        if num2<0:
             return -1 + self.sum(num1,num2+1)
