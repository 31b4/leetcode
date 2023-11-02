class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    return [sorted(nums).index(a) for a in nums]
