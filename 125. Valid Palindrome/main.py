class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ''
        for c in s.lower():
            if c.isalnum():
                ans += c

        return ans==ans[::-1]
