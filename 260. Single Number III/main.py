class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        result: list[int] = [0, 0]
        index = 0

        for i in range(n):
            found = False
            for j in range(n):
                if i != j and nums[i] == nums[j]:
                    found = True
                    break
            if not found:
                result[index] = nums[i]
                index += 1
                if index == 2:
                    break

        return result
