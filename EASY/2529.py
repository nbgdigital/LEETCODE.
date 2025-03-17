class Solution:
  def maximumCount(self, nums: list[int]) -> int:
    return max(sum(n > 0 for n in nums), sum(n < 0 for n in nums))
