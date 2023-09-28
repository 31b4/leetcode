class Solution:
    def intToRoman(self, num: int) -> str:
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D","DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L","LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX"]
        ans = m[num // 1000]
        ans += c[(num%1000) // 100]
        ans += x[(num%100) // 10]
        ans += i[(num%10)]

        return ans
