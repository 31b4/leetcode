class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0
        svline = []
        while i < len(words):
            if len(" ".join(svline))+len(words[i])+1 <= maxWidth or len(svline) == 0:
                svline.append(words[i])
                i+=1
            elif len(" ".join(svline)) == maxWidth:
                ans.append(" ".join(svline))
                svline = []
            else:
                leftSpaces = maxWidth - len("".join(svline))
                sv = ""
                if i == len(words):
                    leftSpaces = maxWidth - len(" ".join(svline))
                    sv = " ".join(svline) + (" "*leftSpaces)
                if len(svline) == 1:
                    minimumSpaces = leftSpaces
                    leftOverSpaces = 0
                    sv += svline[0] + (" "*minimumSpaces)
                else:
                    minimumSpaces = leftSpaces // (len(svline)-1)
                    leftOverSpaces = leftSpaces % (len(svline)-1)
                    for x in svline[:-1]:
                        sv += x + (" "*minimumSpaces)
                        if leftOverSpaces > 0:
                            sv+=" "
                            leftOverSpaces -=1
                    sv+=svline[-1]
                print(sv)
                ans.append(sv)
                svline = []
        if len(svline) > 0:
            leftSpaces = maxWidth - len(" ".join(svline))
            ans.append(" ".join(svline) + (" " * leftSpaces))
        return ans
