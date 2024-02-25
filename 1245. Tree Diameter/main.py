class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def max_depth(node, prev_node = None):
            depth, farthest_node = 0, node
            for nnode in tree[node]:
                if nnode != prev_node:
                    d, fn = max_depth(nnode, node)
                    if 1 + d > depth:
                        depth, farthest_node = 1 + d, fn
            return depth, farthest_node
        
        _, farthest_node = max_depth(0)
        diameter, _ = max_depth(farthest_node)
        return diameter
