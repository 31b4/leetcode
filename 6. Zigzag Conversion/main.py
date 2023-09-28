class Solution:
    def convert(self, s: str, numRows: int) -> str:
        x = 0
        rows = [""]*numRows
        while True:
            if x == len(s):
                break
            for i in range(0, numRows):
                if x == len(s):
                    break
                rows[i] += s[x]
                x += 1

            for i in range(numRows-2, 0, -1):
                if x == len(s):
                    break
                rows[i] += s[x]
                x += 1
        return "".join(rows)
