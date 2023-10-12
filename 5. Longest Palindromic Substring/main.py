class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(0,len(s)):
            for j in range(i+1+len(ans),len(s)+1):
                word = s[i:j]
                print(word)
                if word == word[::-1]:
                    ans = word
        return ans
