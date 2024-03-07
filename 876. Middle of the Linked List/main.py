class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = head
        fast_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer
