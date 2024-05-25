class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        word_set = set(wordDict)
        return self.wordBreakHelper(s, 0, word_set, memo)
    
    def wordBreakHelper(self, s: str, start: int, word_set: set, memo: dict) -> List[str]:
        if start in memo:
            return memo[start]
        
        valid_substr = []
        
        if start == len(s):
            valid_substr.append("")
        for end in range(start + 1, len(s) + 1):
            prefix = s[start:end]
            if prefix in word_set:
                suffixes = self.wordBreakHelper(s, end, word_set, memo)
                for suffix in suffixes:
                    valid_substr.append(prefix + ("" if suffix == "" else " ") + suffix)
        
        memo[start] = valid_substr
        return valid_substr
