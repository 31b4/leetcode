class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1000000007
        a = e = i = o = u = 1

        for length in range(2, n + 1):
            new_a = (e + u + i) % MOD
            new_e = (a + i) % MOD
            new_i = (e + o) % MOD
            new_o = i % MOD
            new_u = (o + i) % MOD

            a, e, i, o, u = new_a, new_e, new_i, new_o, new_u

        count = (a + e + i + o + u) % MOD
        return int(count)
