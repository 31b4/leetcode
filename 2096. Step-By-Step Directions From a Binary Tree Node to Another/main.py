class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        q: list[TreeNode] = [root]
        while q:
            cur_node: TreeNode = q.pop()
            if cur_node.val == startValue:
                start_node = cur_node  # here we're setting up the start node
                break

            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)

        # child node value -> TreeNode object which is parent to node with this value
        nodes_parents: dict[int, TreeNode] = {}
        q = [root]
        while q:
            cur_node = q.pop()
            if cur_node.left:
                nodes_parents[cur_node.left.val] = cur_node
                q.append(cur_node.left)
            if cur_node.right:
                nodes_parents[cur_node.right.val] = cur_node
                q.append(cur_node.right)

        visited = set()
        q = [start_node]
        # key is the destination node to which we travel - value is a tuple with 2 elements - (source_node, direction)
        tracked_path: dict[TreeNode, tuple(TreeNode, str)] = {}

        while q:
            cur_node = q.pop()
            visited.add(cur_node)

            if cur_node.val == destValue:
                destination_node = cur_node
                break  # we've reached the target node

            if cur_node.val in nodes_parents and nodes_parents[cur_node.val] not in visited:
                parent = nodes_parents[cur_node.val]
                q.append(parent)
                tracked_path[parent] = (cur_node, "U")  # this is parent node, we go up

            if cur_node.left and cur_node.left not in visited:
                q.append(cur_node.left)
                tracked_path[cur_node.left] = (cur_node, "L")

            if cur_node.right and cur_node.right not in visited:
                q.append(cur_node.right)
                tracked_path[cur_node.right] = (cur_node, "R")

        # Now we need to construct path in a string from tracked_path we have
        result_path: list[str] = []
        cur_node = destination_node

        while cur_node != start_node:
            source_node, direction = tracked_path[cur_node]
            result_path.append(direction)  # directions will be in reversed order
            cur_node = source_node

        result_path.reverse()
        return "".join(result_path)
