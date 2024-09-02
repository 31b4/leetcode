class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        for i in range(1, len(chalk)):
            chalk[i]+=chalk[i-1]
        k%=chalk[-1]
        return bisect.bisect_right(chalk, k)
        
