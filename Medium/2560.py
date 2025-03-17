class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def cap(c):
            cn = 0
            i = 0
            while i < len(nums):
                if nums[i] <= c:
                    cn += 1
                    i += 1
                i += 1
            return cn >= k
        
        l, r = min(nums), max(nums)

        while l < r:
            mid = (l + r) // 2
            if cap(mid):  
                r = mid
            else:
                l = mid + 1
        return l
