class Solution:
    def myAtoi(self, s: str) -> int:
        sv = ""
        for x in s:
            if sv != "" and not x.isnumeric():
                break
            if sv == "" and x == "-" or x == "+":
                sv += x
            elif x.isnumeric():
                sv += x
            elif x.isalpha() or x == ".":
                break
            
        if sv == "":
            return 0
        print(sv)
        if not sv[0].isnumeric() and len(sv) == 1:
            return 0
        

        if int(sv) > 2**31-1:
            return 2**31-1
        if int(sv) < -2**31:
            return -2**31
        return int(sv)
