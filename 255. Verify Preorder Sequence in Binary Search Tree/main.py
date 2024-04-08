class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_allowed = float("-inf")  # Initialize the minimum allowed value
        stack = []  # Initialize the stack to keep track of nodes
        for node_val in preorder:  # Iterate through each node in the preorder traversal
            while stack and stack[-1] < node_val:  # Pop elements from stack until it's empty or top is greater than current node value
                min_allowed = stack.pop()  # Update the minimum allowed value
            if node_val < min_allowed:  # If the current node value is less than the minimum allowed value
                return False  # Not a valid preorder sequence
            stack.append(node_val)  # Push the current node value to stack
        return True  # If the entire traversal is valid, it's a valid preorder sequence
