from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            counter = defaultdict(int)
            distinct = 0
            left = 0
            result = 0

            for right in range(len(nums)):
                if counter[nums[right]] == 0:
                    distinct += 1
                counter[nums[right]] += 1

                while distinct > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        distinct -= 1
                    left += 1

                result += right - left + 1

            return result

        return atMostK(nums, k) - atMostK(nums, k - 1)
