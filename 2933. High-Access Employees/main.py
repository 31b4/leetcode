class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        eDict = defaultdict(list)
        for e, t in access_times:
            eDict[e].append(int(t))

        res = []
        for e, t in eDict.items():
            t.sort()
            n = len(t)
            for i in range(n - 2):
                if t[i + 2] - t[i] < 100:
                    res.append(e)
                    break

        return res
