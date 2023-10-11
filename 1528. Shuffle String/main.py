class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join([x[0] for x in sorted(zip(s, indices), key=lambda z: z[1])])
