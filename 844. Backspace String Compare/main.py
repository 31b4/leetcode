class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def solve(string):
            while '#' in string:
                string = re.sub(r'^#|[a-z]#', '', string)
            return string
        return solve(s) == solve(t)
