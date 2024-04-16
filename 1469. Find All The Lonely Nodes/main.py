class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
      self.lonely_nodes = []

      def dfs(node):
		# We'll append the child's value only if it is an only child
        if node.left and not node.right:
          self.lonely_nodes.append(node.left.val)
        if node.right and not node.left:
          self.lonely_nodes.append(node.right.val)
		  
		# Then dfs left and/or right, whichever is present
        if node.left:
          dfs(node.left)
        if node.right:
          dfs(node.right)

      dfs(root)
      return self.lonely_nodes
