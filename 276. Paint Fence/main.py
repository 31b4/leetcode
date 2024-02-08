class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0: return 0 
        if n == 1: return k 
        if n == 2: return k * k 
        table = [0, k, k*k] + [-1] * (n-2)
        print(table)
        for i in range(3, n + 1):
            table[i] = (table[i-1] + table[i-2]) * (k-1)
        
        return table[n]
