# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummy = res = PolyNode()
        
        while poly1 and poly2:
            if poly1.power == poly2.power:
                if poly1.coefficient + poly2.coefficient != 0:
                    res.next = PolyNode(poly1.coefficient + poly2.coefficient, poly1.power)
                    poly1 = poly1.next
                    poly2 = poly2.next
                else:
                    poly1 = poly1.next
                    poly2 = poly2.next
                    continue

            elif poly1.power > poly2.power:
                res.next = PolyNode(poly1.coefficient, poly1.power)
                poly1 = poly1.next
            else:
                res.next = PolyNode(poly2.coefficient, poly2.power)
                poly2 = poly2.next
            res = res.next
        
        while poly1:
            res.next = PolyNode(poly1.coefficient, poly1.power)
            poly1 = poly1.next
            res = res.next
        
        while poly2:
            res.next = PolyNode(poly2.coefficient, poly2.power)
            poly2 = poly2.next
            res = res.next

        return dummy.next
