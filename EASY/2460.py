class Solution:
  def applyOperations(self, nums: list[int]) -> list[int]:
    a = [0] * len(nums)

    for i in range(len(nums) - 1):
      if nums[i] == nums[i + 1]:
        nums[i] *= 2
        nums[i + 1] = 0

    i = 0
    for n in nums:
      if n > 0:
        a[i] = n
        i += 1

    return a
