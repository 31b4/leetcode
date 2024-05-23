class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        self.res = False

        def backtrack(string, idx, pattern_dict):
            if not string:
                if idx == len(pattern):
                    self.res = True
                return
            if idx == len(pattern):
                return
            
            curr_pattern = pattern[idx] # pointer to the current pattern (character)
            for i in range(len(string)):
                part = string[:i+1] # Substring we are going to use to look for matching
                part_after = string[i+1:] # Substring that is left over
                if curr_pattern not in pattern_dict and part not in pattern_dict.values(): # This part checks if the substring we are looking for matching has not been seen before
                    pattern_dict[curr_pattern] = part
                    backtrack(part_after, idx+1, pattern_dict)
                    del pattern_dict[curr_pattern] # backtracking this pattern
                elif curr_pattern in pattern_dict and pattern_dict[curr_pattern] == part: # This part checks if the current pattern exists and if it matches the current substring we are looking at
                    backtrack(part_after, idx+1, pattern_dict)
            
        backtrack(s, 0, {})
        return self.res
