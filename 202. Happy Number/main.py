class Solution:
    def isHappy(self, n: int) -> bool:
        visted = set()
        while n != 1 and n not in visted:
            visted.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1
