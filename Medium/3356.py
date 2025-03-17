class Solution:
  def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
    magic = [0] * (len(nums) + 1)
    total_magic = 0
    spell_count = 0

    for i, candy in enumerate(nums):
      while total_magic + magic[i] < candy:
        if spell_count == len(queries):
          return -1
        start, end, power = queries[spell_count]
        spell_count += 1
        if end < i:
          continue
        magic[max(start, i)] += power
        if end + 1 < len(magic):
          magic[end + 1] -= power
      total_magic += magic[i]

    return spell_count
