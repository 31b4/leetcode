# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even=True
        q=deque([root])
        while q:
            prev=float("-inf") if even else float("inf")
            for _ in range(len(q)):
                n = q.popleft()
                if even and (n.val%2==0 or n.val<=prev):
                    return False
                if not even and (n.val%2==1 or n.val>=prev):
                    return False
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                prev=n.val
            even=not even
        return True
                
