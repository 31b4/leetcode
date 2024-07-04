# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr=head.next, head.next
        sum=0
        while curr:
            x=curr.val
            if x!=0: sum+=x
            else:
                prev.val=sum
                prev.next=curr.next
                prev=prev.next
                sum=0
            curr=curr.next
        return head.next
        
