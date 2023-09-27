class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()
        median = 0
        if len(merged_array) %2 != 0:
            median = merged_array[len(merged_array) // 2]
        else:
            if len(merged_array) > 1:
                median = (merged_array[len(merged_array)//2-1] + merged_array[len(merged_array)//2]) /2
            else:
                median = merged_array[0]
        return median
