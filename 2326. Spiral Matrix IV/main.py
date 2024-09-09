# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        generatedMatrix = [[0 for i in range(n)] for j in range(m)]
        left= 0
        right=n
        top= 0
        bottom=m 
        while left < right and top < bottom :
            for i in range(left, right):
                if not head:
                    generatedMatrix[top][i] = -1
                else:
                    generatedMatrix[top][i] = head.val
                    head = head.next
            top += 1
            
            for i in range(top, bottom):
                if not head:
                    generatedMatrix[i][right-1] = -1
                else:
                    generatedMatrix[i][right-1] = head.val
                    head = head.next
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            for i in range(right-1, left-1, -1):
                if not head:
                    generatedMatrix[bottom-1][i] = -1
                else:
                    generatedMatrix[bottom-1][i] = head.val
                    head = head.next 
            bottom -= 1
            
            for i in range(bottom-1, top-1, -1):
                if not head:
                    generatedMatrix[i][left] = - 1
                else:
                    generatedMatrix[i][left] = head.val
                    head = head.next
            left += 1
        return generatedMatrix 
