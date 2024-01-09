# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def bfs(queue):

            leaf_node = []
            while queue:

                current = queue.pop()

                if not current.left and not current.right:
                    leaf_node.append(current.val)

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            return leaf_node

        queue = collections.deque([root1])
        leaf1 = bfs(queue)
        queue = collections.deque([root2])
        leaf2 = bfs(queue)

        return leaf1 == leaf2

        

