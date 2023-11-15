class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i in range(len(boxes)):
            sv = 0
            for j in range(len(boxes)):
                if(boxes[j] == '1'):
                    sv += abs(i- j)
            res.append(sv)
        return res
