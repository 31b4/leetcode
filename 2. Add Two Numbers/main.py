# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        cur =  ans
        leftover = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            summa = x + y + leftover
            leftover = summa // 10
            cur.next = ListNode(summa % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if leftover:
            cur.next = ListNode(leftover)
        return ans.next
