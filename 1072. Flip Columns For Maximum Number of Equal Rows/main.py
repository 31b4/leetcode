class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = {}
        
        for row in matrix:
            # Normalize the row pattern
            # If the first element is 0, keep the row as is
            # If the first element is 1, take the complement of the row
            normalized = tuple(cell if row[0] == 0 else 1 - cell for cell in row)
            
            # Count the occurrences of each normalized pattern
            if normalized not in pattern_count:
                pattern_count[normalized] = 0
            pattern_count[normalized] += 1
        
        # The maximum value in pattern_count is the answer
        return max(pattern_count.values())
