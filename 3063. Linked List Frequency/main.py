# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freqs = {}
        out_head = ListNode()
        latest_node = out_head
        while head:
            node = freqs.get(head.val)
            if node:
                node.val += 1
            else:
                node = ListNode(1)
                latest_node.next = node
                latest_node = node
                freqs[head.val] = latest_node
                
            head = head.next

        return out_head.next
        
