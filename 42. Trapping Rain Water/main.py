class Solution:# done using two pointers
    def trap(self, H: List[int]) -> int:
        L = 0
        R = len(H) - 1
        Lmax = 0
        Rmax = 0
        ans = 0
        while L <= R:
            if H[L] <= H[R]:
                Lmax = max(Lmax, H[L])
                ans += Lmax - H[L]
                L += 1
            else:
                Rmax = max(Rmax, H[R])
                ans += Rmax - H[R]
                R -= 1
        return ans
