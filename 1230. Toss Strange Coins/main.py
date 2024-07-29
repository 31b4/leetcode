class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        length = len(prob) - target + 1

        dp, comp = [1.0] * length, [1-p for p in prob]
        for i in range(length-1):
            dp[i+1] = dp[i] * comp[i]

        for i in range(target):
            dp[0] *= prob[0]
            for j in range(1, length):
                dp[j] = dp[j-1] * comp[j] + dp[j] * prob[j]
            prob.pop(0), comp.pop(0)

        return dp[-1]
