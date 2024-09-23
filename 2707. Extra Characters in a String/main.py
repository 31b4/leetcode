class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Convert the dictionary list into a set for O(1) lookup time
        wordSet = set(dictionary)
        n = len(s)
        
        # dp[i] will store the minimum extra characters in the substring s[i:]
        dp = [0] * (n + 1)
        
        # Fill dp array from right to left
        for i in range(n - 1, -1, -1):
            # By default, we assume the current character is extra
            dp[i] = dp[i + 1] + 1
            
            # Try to match any word from dictionary starting at index i
            for length in range(1, n - i + 1):
                if s[i:i + length] in wordSet:
                    dp[i] = min(dp[i], dp[i + length])
        
        # The answer is the number of extra characters in the entire string
        return dp[0]
