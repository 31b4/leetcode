class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @cache
        def f(n, k):
            if k==0: return 1
            if k<0 or n<=0: return 0
            return (f(n-1, k)+f(n, k-1)-f(n-1, k-n)+10**9+7)%(10**9+7)
        return f(n, k)
