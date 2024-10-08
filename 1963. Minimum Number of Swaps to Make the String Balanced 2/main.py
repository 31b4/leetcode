class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        max_imbalance = 0
        
        # Traverse the string
        for char in s:
            if char == '[':
                balance += 1  # Opening bracket, increase balance
            else:
                balance -= 1  # Closing bracket, decrease balance
            
            # Track the maximum imbalance (i.e., the maximum negative balance)
            if balance < 0:
                max_imbalance = max(max_imbalance, -balance)
        
        # The number of swaps needed is half of the max imbalance
        # because each swap fixes two imbalances (one opening, one closing).
        return (max_imbalance + 1) // 2
