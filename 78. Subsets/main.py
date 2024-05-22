class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def explore(index, curr):
            if index == len(nums):
                result.append(curr.copy())
                return

            curr.append(nums[index])
            explore(index + 1, curr)
            curr.pop()
            explore(index + 1, curr)

        explore(0, [])
        return result
