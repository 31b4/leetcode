class Solution:
    def findBottomLeftValue(self, root):
        last = 0
        q = deque([root])

        while q:
            count = len(q)
            for i in range(count):
                curr = q.popleft()
                if i == 0:
                    last = curr.val  # last leftMost val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return last
