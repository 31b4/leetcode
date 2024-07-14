# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        counter = defaultdict(int)
        node = head
        while node:
            counter[node.val] += 1
            node = node.next
        while head:
            if counter[head.val] == 1:
                break
            head = head.next
        if not head:
            return None
        node = prev = head
        while node:
            if counter[node.val] == 1:
                if prev != node:
                    prev.next = node
                prev = node
            node = node.next
        prev.next = None
        return head
