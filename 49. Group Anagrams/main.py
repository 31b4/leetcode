class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            temp = ''.join(sorted(word))
            if temp not in d:
                d[temp] = [word]
            else:
                d[temp].append(word)
        return d.values()
