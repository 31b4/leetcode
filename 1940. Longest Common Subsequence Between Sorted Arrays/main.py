class Solution:
    def longestCommonSubsequence(self, A):
        return (lambda count: [i for i in sorted(count) if count[i] == len(A)]) (reduce(lambda p, c: p + Counter(c), A, Counter()))
