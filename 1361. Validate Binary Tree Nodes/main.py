class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # find root
        left = set(leftChild)
        right = set(rightChild)
        
        root = -1
        for node in range(n):
            if node not in left and node not in right:
                if root != -1: return False # should only 1 root node
                root = node
        
        visited = set()
        def dfs(node):
            if node in visited: return inf # cycle
            visited.add(node)

            cnt = 1
            if leftChild[node] != -1:
                cnt += dfs(leftChild[node])
            if rightChild[node] != -1:
                cnt += dfs(rightChild[node])
            return cnt
        return dfs(root) == n
