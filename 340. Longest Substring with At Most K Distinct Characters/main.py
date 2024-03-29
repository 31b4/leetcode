class Solution:
    
    def lengthOfLongestSubstringKDistinct(self, string: str, numDistinctCharacters: int) -> int:
        
        # create a counter that will store the frequency of characters
        freq = Counter()
        
        # create a variable to store the index of the left side of the window
        window_start = 0
        
        # create a variable to return that will hold the length of the longest valid substring seen
        longest_valid_substring_seen = 0
        
        # iterate through the entire string, "window_end" represents the "right side" of the window
        for window_end, char in enumerate(string):
            
            # load up the frequency counter until constraint violation
            freq[char] += 1
            
            # shrink the window if violates the constraint of more than the number of distinct characters
            # the length of the freq counter represents the number of distinct characters
            while len(freq) > numDistinctCharacters:
                
                # get the left char of the window (the char that window_start points to)
                left_char = string[window_start]
                
                # and decrement it in the counter
                freq[left_char] -= 1
                
                # IMPORTANT: we check the length of the frequency counter (which is equivalent to number of distinct chars)
                # we must delete chars that have a zero count, because we no longer have a distinct char in window
                if freq[left_char] == 0:
                    del freq[left_char]
                
                # shrink window here
                window_start += 1
            
            # valid window at this point, get the size of the window
            # and compare it to the longest valid substring seen so far
            # update longest_valid_substring_seen if we found a new longest valid substring
            window_size = window_end - window_start+1
            longest_valid_substring_seen = max(longest_valid_substring_seen, window_size)
        
        return longest_valid_substring_seen
