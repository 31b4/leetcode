class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # 1. We'll start by copying the shortest of the arrays.
        # 2. Then we'll remove elements that don't appear in the other arrays.
        # 3. Beacuse all arrays are sorted, we can use binary search to check for elements in the other arrays.
        #
        # T( l * (log(m) + log(n)) ) where l is the shortest array, and m, and n are the other two.
        # S( 1 ) we copy the array at cost S( l ), but we don't count the answer as part of the space complexity.
        
        # 3. Binary search function
        def find(x: int, arr: List[int]) -> bool:
            i = 0
            j = len(arr) - 1
            while i <= j:
                mid = (j + i) // 2
                if arr[mid] < x:
                    i = mid + 1
                elif x < arr[mid]:
                    j = mid - 1
                else:
                    return True
            return False

        # Ensure arr1 is the shortest, but we don't care about the relative lengths of arr2 and arr3
        if len(arr2) > len(arr3):
            arr2, arr3 = arr2, arr3
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        
        # 1. Copy the shortest array
        ans = arr1[:]

        # Filter out elements in T(l * (log(m) + log(n)) )
        # We do this by shifting numbers in the array as we go,
        # Then we pop off the extra numbers at the end.
        # This gives us T(n) complexity and requires only S(1) space.
        offset = 0
        for i, x in enumerate(ans):
            if not (find(x, arr2) and find(x, arr3)):
                offset += 1
            else:
                ans[i - offset] = ans[i]
        
        for _ in range(offset):
            ans.pop()
        
        return ans
