class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0 # Initialize count to keep track of consecutive odd numbers

        for num in arr: # Iterate through each element in the array
            if num % 2 != 0: # Check if the current element is odd
                count += 1 # Increment the count if it's odd
                if count == 3: # If we have found three consecutive odds, return true
                    return True
            else: # If the element is even, reset the count to 0
                count = 0

        return False # If we finish the loop without finding three consecutive odds, return false
