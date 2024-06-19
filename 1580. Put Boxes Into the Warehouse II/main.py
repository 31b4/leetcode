class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:


        l, r = [h for h in warehouse], [h for h in warehouse]
        for i in range(1, len(warehouse)):
            l[i] = min(l[i], l[i - 1])
            r[-i - 1] = min(r[-i - 1], r[-i])
        ht = [0 for _ in range(len(warehouse))]
        for i in range(len(warehouse)):
            ht[i] = max(l[i], r[i])
        
        print(ht)

        res = 0
        ht.sort()
        boxes.sort()
        for h in ht:
            if res < len(boxes) and boxes[res] <= h: res += 1
        
        return res
      
