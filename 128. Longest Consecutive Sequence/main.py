class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0

        temp = sorted(list(set(nums)))
        i = 0
        j = 1
        count = 1
        curr = 1

        while j < len(temp):
            if temp[j] - 1 == temp[i]:
                curr += 1
                count = max(curr, count)
            else:
                curr = 1
            i = j
            j += 1
        return count
