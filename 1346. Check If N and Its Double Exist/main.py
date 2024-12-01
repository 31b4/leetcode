class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Use a set to track visited numbers
        seen = set()
        for num in arr:
            # Check if the current number's double or half (if even) is in the set
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            # Add the current number to the set
            seen.add(num)
        return False
