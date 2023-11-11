class Solution:
    def stringCount(self, n: int) -> int:
        if(n<4):
            return 0
        a=26**n
        b=25**n
        c=24**n
        d=23**n
        return ((a)-(3*b+(n*(b//25))-3*c-(2*n*(c//24))+d+(n*(d//23))))%1000000007
