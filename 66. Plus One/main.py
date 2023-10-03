class Solution:
    def plusOne(self, D: List[int]) -> List[int]:
        return list(map(int,list(str(int("".join(list(map(str,D))))+1))))
