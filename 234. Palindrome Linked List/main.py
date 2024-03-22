class Solution(object):
    def isPalindrome(self, head):
        slow = fast = head 
        while fast and fast.next:
           fast = fast.next.next
           slow = slow.next 
            
        stack1=[]
        stack2 = []
        
        fast = slow 
        slow = head
        while fast:
            stack2.append(slow.val)
            stack1.append(fast.val)
            fast = fast.next
            slow = slow.next 
            
        stack2.reverse()
        return stack1 == stack2
        
