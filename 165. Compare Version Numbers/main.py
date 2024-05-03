class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def helper(s: str, idx: int) -> List[int]:
            num = 0
            while idx < len(s):
                if s[idx] == '.':
                    break
                else:
                    num = num * 10 + int(s[idx])
                idx += 1
            return [num, idx+1]

        i = j = 0
        while(i < len(version1) or j < len(version2)):
            v1, i = helper(version1, i)
            v2, j = helper(version2, j)
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        return 0
