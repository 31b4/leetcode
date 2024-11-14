class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(max_products: int) -> bool:
            # Calculate the number of stores needed for each product type
            stores_needed = sum((quantity + max_products - 1) // max_products for quantity in quantities)
            # Check if we can manage with `n` stores
            return stores_needed <= n

        # Binary search range
        left, right = 1, max(quantities)
        
        # Perform binary search
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid  # Try for a smaller max
            else:
                left = mid + 1  # Increase max products per store
        
        return left
