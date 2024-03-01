# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even = 0
        odd = 0
        while head is not None:
            e = head.val
            o = head.next.val
            head = head.next.next
            if e > o:
                even += 1
            else:
                odd += 1
        if even == odd:
            return "Tie"
        elif even > odd:
            return "Even"
        return "Odd"
