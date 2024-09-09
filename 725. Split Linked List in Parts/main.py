# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.

class Solution:
    def splitListToParts(self, head, k):
        ans = [None] * k

        # Calculate total size of the linked list
        size = 0
        current = head
        while current:
            size += 1
            current = current.next

        # Minimum size of each part
        split_size = size // k
        remainder = size % k  # Remaining nodes to distribute

        current = head
        for i in range(k):
            ans[i] = current
            current_size = split_size + (1 if remainder > 0 else 0)
            remainder -= 1

            # Traverse to the end of the current part
            for _ in range(current_size - 1):
                if current:
                    current = current.next

            # Cut the list
            if current:
                next_part = current.next
                current.next = None
                current = next_part

        return ans
