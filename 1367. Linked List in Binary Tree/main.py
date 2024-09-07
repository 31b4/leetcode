class Solution:
    def isSubPath(self, head, root):
        def checkPath(head, root):
            if not head: return True
            if not root or head.val != root.val: return False
            return checkPath(head.next, root.left) or checkPath(head.next, root.right)

        if not root: return False
        if checkPath(head, root): return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
