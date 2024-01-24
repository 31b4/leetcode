class Solution:
    def pseudoPalindromicPaths(self, root):
        count = 0
        stack = [(root, 0)]

        while stack:
            node, path = stack.pop()

            if node:
                path ^= 1 << node.val

                if not node.left and not node.right:
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))

        return count

