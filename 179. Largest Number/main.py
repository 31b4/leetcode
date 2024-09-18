from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert numbers to strings for concatenation
        num_strs = list(map(str, nums))
        
        # Custom comparator: Compare which combination of two strings gives a larger number
        def compare(x, y):
            if x + y > y + x:
                return -1  # x should come before y
            elif x + y < y + x:
                return 1   # y should come before x
            else:
                return 0   # they are equal in terms of ordering
        
        # Sort the list using the custom comparator
        num_strs.sort(key=cmp_to_key(compare))
        
        # Join the sorted strings into the largest number
        largest_num = ''.join(num_strs)
        
        # Edge case: if the largest number starts with '0', return '0'
        return '0' if largest_num[0] == '0' else largest_num
