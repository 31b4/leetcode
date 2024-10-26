from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depths = {}
        heights = {}
        
        # Step 1: Compute heights and depths using DFS
        def compute_heights(node, depth):
            if not node:
                return -1
            depths[node.val] = depth
            left_height = compute_heights(node.left, depth + 1)
            right_height = compute_heights(node.right, depth + 1)
            heights[node.val] = 1 + max(left_height, right_height)
            return heights[node.val]
        
        compute_heights(root, 0)
        
        # Step 2: Precompute the maximum heights for each level excluding subtrees
        max_height_without_subtree = {}
        level_max_height = {}
        
        # Collect the max heights for each depth level
        def update_level_heights(node):
            if not node:
                return
            depth = depths[node.val]
            if depth not in level_max_height:
                level_max_height[depth] = []
            level_max_height[depth].append(heights[node.val])
            update_level_heights(node.left)
            update_level_heights(node.right)
        
        update_level_heights(root)
        
        # Sort each level's heights in descending order to allow easy access to the top two heights
        for depth in level_max_height:
            level_max_height[depth].sort(reverse=True)
        
        # Compute maximum height of the tree excluding each node's subtree
        for node_val in heights:
            depth = depths[node_val]
            max_heights = level_max_height[depth]
            
            # Determine the max height excluding the subtree at this node
            if len(max_heights) == 1:
                max_height_without_subtree[node_val] = depth - 1
            elif heights[node_val] == max_heights[0]:
                max_height_without_subtree[node_val] = depth + (max_heights[1] if len(max_heights) > 1 else 0)
            else:
                max_height_without_subtree[node_val] = depth + max_heights[0]
        
        # Step 3: Answer each query
        return [max_height_without_subtree[q] for q in queries]
